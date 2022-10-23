import requests


# URL: http://vcm-7631.vm.duke.edu:5002
def get_ids():
    r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sk591")
    print(r.status_code)
    dict_id = r.json()
    return dict_id
    # {'Donor': 'M1', 'Recipient': 'F6'} in json


def get_bloodtype():
    r1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1")
    r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
    print(r1.status_code)
    print(r2.status_code)
    type1 = r1.text  # donor
    type2 = r2.text  # recipient
    types = (type1, type2)
    return types
    # ('O+', 'AB-') in tuple


# O+ cannot donate to AB-
def check_match():
    out_data = {"Name": "sk591", "Match": "No"}
    r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                      json=out_data)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    # dict_id = get_ids()
    # print(dict_id)
    # dict_type = get_bloodtype()
    # print(dict_type)
    check_match()
