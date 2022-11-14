import pytest
from database_definition import Patient
from pymodm import errors as pymodm_errors

# Run function from server that connects to MongoDB.  This is run outside
#   any test function so that the connection is made for all unit tests.
from db_server import init_server
init_server()


@pytest.mark.parametrize("in_data, expected_keys, expected_types, expected", [
    ({"a": 1, "b": "string"}, ["a", "b"], [int, str], True),
    ({"a": 1, "b": 2}, ["a", "b"], [int, str],
     "Key b's value has the wrong data type"),
    ({"c": 1, "b": "string"}, ["a", "b"], [int, str],
     "Key a is missing from POST data"),
    (["a", "b", 1, 2], ["a", "b"], [int, str],
     "POST data was not a dictionary"),
    ({"a": "1", "b": "string"}, ["a", "b"], [int, str],
     "Key a's value has the wrong data type"),
    ({"a": 1, "b": "string", "c": True}, ["a", "b"], [int, str], True),
])
def test_dictionary_validation(in_data, expected_keys, expected_types,
                               expected):
    from db_server import dictionary_validation
    answer = dictionary_validation(in_data, expected_keys, expected_types)
    assert answer == expected


def test_add_patient():
    # import function to test as well as function to connect to MongoDB
    #   database
    from db_server import add_patient
    # Create data for the patient
    patient_name = "David"
    patient_id = 222
    blood_type = "A+"

    # Option 1: function being tested returns a Patient instance with copy of
    #           what was saved to MongoDB.  So, call function and receive
    #           the result.  Use that result to call the ".delete()" method of
    #           the MongoModel-type class to remove the entry from the MongoDB
    #           database, then assert that the saved name matches the name
    #           sent in this test.
    answer = add_patient(patient_name, patient_id, blood_type)
    answer.delete()
    assert answer.name == patient_name

    # Option 2: function being tested does not return a Patient instance.  So,
    #           call function.  Then, separately query database for the
    #           record which should have been added.  Delete that record in
    #           the MongoDB database, then assert that the found record name
    #           matched the name sent in this test.
    # add_patient(patient_name, patient_id, blood_type)
    # find_patient = Patient.objects.raw({"_id": patient_id}).first()
    # find_patient.delete()
    # assert answer.name == patient_name

    # Overall approach to writing a test of database functions:
    # 1. Set up the database with the needed data
    # 2. Run code that you want to test
    # 2b. Get updated info from database for comparison
    # 3. Clean up database
    # 4. Assert


@pytest.mark.parametrize("in_data, expected", [
    ({"name": "Good Input", "id": 123, "blood_type": "A+"},
     ("Patient successfully added", 200)),
    ({"name": "Bad Input", "id": 234, "blxxd_type": "A+"},
     ("Key blood_type is missing from POST data", 400)),
])
def test_add_new_patient_worker(in_data, expected):
    from db_server import add_new_patient_worker
    answer = add_new_patient_worker(in_data)
    try:
        patient_to_remove = \
            Patient.objects.raw({"_id": in_data["id"]}).first()
    except pymodm_errors.DoesNotExist:
        pass
    else:
        patient_to_remove.delete()
    assert answer == expected


def test_add_test_to_patient():
    from db_server import add_patient, add_test_to_patient
    # Set up my database for test
    patient_id = 123
    patient_name = "David"
    added_patient = add_patient(patient_name, patient_id, "A+")

    # run code to test
    test_name = "XXX"
    test_result = 200
    out_data = {"id": patient_id,
                "test_name": test_name,
                "test_result": test_result}
    add_test_to_patient(out_data)

    patient_from_db = Patient.objects.raw({"_id": patient_id}).first()

    # clean up database
    added_patient.delete()

    # asserts
    assert patient_from_db.test_name[-1] == test_name
    assert patient_from_db.test_result[-1] == test_result


@pytest.mark.parametrize("in_data, expected", [
    ({"id": 123, "test_name": "Good Test", "test_result": 222},
     ("Successfully added test.", 200)),
    ({"id": 123, "test_name": "Bad Test", "test_result": "xxx"},
     ("Key test_result's value has the wrong data type", 400)),
])
def test_add_test_worker(in_data, expected):
    from db_server import add_patient, add_test_worker
    # Set-up database by adding a patient that can receive a test
    added_patient = add_patient("Patient Name", in_data["id"], "A+")
    # Run function under test
    answer = add_test_worker(in_data)
    # Clean-up database
    added_patient.delete()
    # Assert
    assert answer == expected


def test_find_patient_success():
    from db_server import add_patient, find_patient
    # Setup database by adding a patient to be found
    patient_name = "Patient to Find"
    patient_id = 345
    added_patient = add_patient(patient_name, patient_id, "A+")
    # Call function to be tested
    found_patient = find_patient(patient_id)
    # cleanup database
    added_patient.delete()
    # Assert
    assert found_patient.name == patient_name
    assert found_patient.id == patient_id


def test_find_patient_not_found():
    from db_server import find_patient
    answer = find_patient(4346343)
    assert answer is False


def test_add_test_to_patient_success():
    from db_server import add_patient, add_test_to_patient
    # Setup database
    patient_id = 123
    added_patient = add_patient("Test Patient", patient_id, "A+")
    # Call function under test
    in_data = {"id": patient_id, "test_name": "HDL", "test_result": 111}
    add_test_to_patient(in_data)
    # Get info from database to see if test was added
    patient_with_test = Patient.objects.raw({"_id": patient_id}).first()
    added_test_name = patient_with_test.test_name[-1]
    added_test_result = patient_with_test.test_result[-1]
    # Clean up database
    added_patient.delete()
    # Assert
    assert added_test_name == "HDL"
    assert added_test_result == 111


def test_add_test_to_patient_patient_not_found():
    from db_server import add_test_to_patient
    in_data = {"id": 333, "test_name": "HDL", "test_result": 111}
    answer = add_test_to_patient(in_data)
    assert answer == ("Patient ID 333 not found in database.", 400)


def test_get_results_worker_success():
    from db_server import add_patient, add_test_to_patient, get_results_worker
    # Setup database
    patient_id = 567
    added_patient = add_patient("Test Patient", patient_id, "A+")
    test_name = "HDL"
    test_result = 333
    add_test_to_patient({"id": patient_id, "test_name": test_name,
                         "test_result": test_result})
    # Call function being tested
    answer, status_code = get_results_worker(str(patient_id))
    # Clean database
    added_patient.delete()
    # Assert
    assert status_code == 200
    assert answer["id"] == patient_id
    assert answer["test_names"] == [test_name]
    assert answer["test_results"] == [test_result]


def test_get_results_worker_fail():
    from db_server import get_results_worker
    answer, status_code = get_results_worker("abc")
    assert answer == "Patient id provided was not an integer"
    assert status_code == 400


@pytest.mark.parametrize("patient_id, expected", [
    ("123", True),
    ("sdb", "Patient id provided was not an integer"),
    ("234", "No patient with id provided was found")
])
def test_validate_patient_id(patient_id, expected):
    from db_server import validate_patient_id, add_patient
    # Setup database
    added_patient = add_patient("Test", 123, "A+")
    # Call function being tested
    answer = validate_patient_id(patient_id)
    # Clean database
    added_patient.delete()
    assert answer == expected