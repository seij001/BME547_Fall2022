# server.py


from flask import Flask, request, jsonify


app = Flask(__name__)


# give decorator to app to access route
@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."
    # I would visit http://127.0.0.1:5000/ to access this route


@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculate blood cholesterol levels\n"
    x += "It is written by Seijung Kim"
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    # usually, the info sent is stored in dictionary
    '''
    incoming_json = {"name": <name_str>,
                     " hdl_value": <hdl_value_int>}
    '''
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The received value was {}".format(hdl_value))
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def add_numbers_to_internet():
    '''
    {"a": 5, "b": 12}
    return sum of these numbers
    '''
    in_data = request.get_json()
    value_a = in_data["a"]
    value_b = in_data["b"]
    sum = value_a + value_b
    # answer = "The sum of {} and {} is {}".format(value_a, value_b, str(sum))
    answer = sum
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
