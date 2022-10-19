import requests


'''
r = requests.get("http://127.0.0.1:5000/info")
print(r.status_code)
print(r.text)
'''


'''
out_data = {"name": "Seijung Kim",
             "hdl_value": 30}
r = requests.post("http://127.0.0.1:5000/hdl_check", json=out_data)
print(r.status_code)
print(r.text)
'''


out_data = {"a": 5, "b": 12}
r = requests.post("http://127.0.0.1:5000/add_numbers", json=out_data)
print(r.status_code)
print(r.text)