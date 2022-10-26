import requests


out_data = {"name": "Charlie", "id": 3, "blood_type": "AB-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
print(r.status_code)
print(r.text)


test_data = {"id": 2, "test_name": "HDL", "test_result": 100}
r = requests.post("http://127.0.0.1:5000/add_test", json=test_data)
print(r.status_code)
print(r.text)
