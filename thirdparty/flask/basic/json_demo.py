from flask import Flask, make_response, jsonify
import json

app = Flask(__name__)


# json is string
@app.route("/", methods=["POST", "GET"])
def index():
    data = {
        "name": "fang",
        "age": 30
    }
    # json.dumps: python dictionary -> json string
    json_str = json.dumps(data)
    return json_str, 200, {"Content-Type": "application/json"}


@app.route("/res", methods=["POST", "GET"])
def res():
    data = {
        "name": "fang",
        "age": 30
    }
    # json.dumps: python dictionary -> json string
    json_str = json.dumps(data)
    resp = make_response(json_str)
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/jsonify", methods=["POST", "GET"])
def _jsonify():
    data = {
        "name": "fang",
        "age": 30
    }
    # return jsonify(data)
    return jsonify(city="shanghai", year=2004)


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
