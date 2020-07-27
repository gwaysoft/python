from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    a = 1/0
    if not all([user_name, password]):
        resp = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(resp)

    if user_name == "admin" and password == "123456":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "invalid admin or password"
        }
        return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
