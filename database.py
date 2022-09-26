def create_patient_entry(patient_name, patient_id,
                         patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    # The empty bracket is an extra list that is a placeholder for now
    # We will store test result here
    return new_patient


def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, id: {}, age: {}".format(patient[0],
                                                 patient[1],
                                                 patient[2]))


def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return False  # when patient is not found


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient[3].append((test_name, test_value))


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_test_to_patient(db, 3, "HDL", 100)
    print(find_patient(db, 3))

    room_list = ["Room 1", "Room 2", "Room 3"]

    for i, patient in enumerate(db):
        # enumerate tells what index I am iterating on
        print(i)
        print("Name = {}, Room: {}".format(patient[0], room))

    for patient, room in zip(db, room_list):
        # use zip when you want to iterate over two loops of same size
        print("Name = {}, Room: {}".format(patient[0], room))


if __name__ == "__main__":
    main()
