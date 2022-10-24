'''
Database format
[{
"name": <string>,
"id": <integer>,
"blood_type": <string>,
"test_name": [<string1>, <string2>, ...],
"test_result": [<string1>, <string2>, ...]
}]

OR

[{
"name": <string>,
"id": <integer>,
"blood_type": <string>,
"tests": {"test_name": [result1, result2 ...]}
}]
'''

db = []  # have this outside to make it global


from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_on():
    return "DB Server is ON"


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {"name": patient_name,
                    "id": patient_id,
                    "blood_type": blood_type,
                    "test_name": [],
                    "test_result": []}
    db.append(new_patient)  # can access db as it's global


def init_server():
    add_patient("Ann Ables", 1, "A+")
    add_patient("Bob Boyles", 2, "B+")
    # can have basic.config here for logging


@app.route("/new_patient", method=["POST"])
def add_new_patient_to_server():
    """
    Receive data from POST request
    Call other functions to do work
    Return info
    """
    # just do the three things
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data["name"],
                in_data["id"],
                in_data["blood_type"])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not dictionary"
    expected_key = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        # zip helps iterate over two lists together
        if type(in_data[key]) is not ex_type:
            # if data type is not as expected
            return "Key {}'s value has the wrong data type".format(key)
    return True  # yes, data is valid


if __name__ == "__main__":
    db = init_server()
    add_patient(db)
    app.run()