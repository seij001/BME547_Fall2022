import requests
'''
r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# needs to be public repo to access
print(r)
print(type(r))
print(r.text)  # result is JSON encoded
print(r.status_code)
if r. status_code == 200:
    answer = r.json()
    print(type(answer))
    for branch in answer:
        print(branch["name"])
answer = r.json()  # puts into a variable matching Python datatype
print(type(answer))
for branch in answer:
    print(branch["name"])

output_info = {"name": "David Ward",
               "net_id": "daw74",
               "e-mail": "david.a.ward@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                  json=output_info)

print(r)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
'''
# in-class exercise:
output_seijung = {"user": "Pranaleerane", "message": "hello"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=output_seijung)
print(r.text)

r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/seij001")
print(r1.text)
