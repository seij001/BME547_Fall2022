import requests


# URL: http://vcm-7631.vm.duke.edu:5002
'''Get the IDs for two patients by making a GET request to URL/get_patients/<name>.
Replace <name> with your Duke Net ID.
This request will return a dictionary in the following format:
{"Recipient": "<ID1>", "Donor": "<ID2>"}.'''


def get_ids():
    r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sk591")
    print(r.status_code)
    dict_id = r.json()
    return dict_id
    # {'Donor': 'M1', 'Recipient': 'F6'} in json



'''
Obtain the blood type of the two patients by making GET requests to URL/get_blood_type/<id> where <id> is replaced by either <ID1> 
or <ID2> from above.
This request will return a string with the blood type of the given patient.'''
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


# Calculate whether it is an acceptable match for the recipient to receive blood from the donor.
# O+ cannot donate to AB-
# O: donate RBC to all, receive from O
# A: donate to A and AB, receive from A and O
# B: donate to B and AB, receive from B and O
# AB: donate to AB, receive from all

'''
Check your result by making a POST request to URL/match_check.
Send a JSON with the following format:
{"Name": "<name>", "Match": "<answer>"}
Replace <name> with your Duke Net ID and <answer> with either Yes or No.
This request will return "Correct" or "Incorrect".'''

def check_match():
    out_data = {"Name": "sk591", "Match": "No"}
    r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    # dict_id = get_ids()
    # print(dict_id)
    # dict_type = get_bloodtype()
    # print(dict_type)
    check_match()
