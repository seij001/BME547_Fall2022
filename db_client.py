import requests

out_data = {"name": "Charlie", "id": 3, "blood_type": "AB-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
print(r.status_code)
print(r.text)

test_data = {"id": 2, "test_name": "HDL", "test_result": 100}
r = requests.post("http://127.0.0.1:5000/add_test", json=test_data)
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/get_results/2")
print(r.status_code)
if r.status_code == 200:
    print(r.json())
else:
    print(r.text)

# Invalid request to see what happens
r = requests.get("http://127.0.0.1:5000/get_results/43")
print(r.status_code)
print(r.text)
