from flask import Flask, session

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/", methods=["POST", "GET"])
def index():
    session["username"] = "sasa"
    session["password"] = "123456"
    return "username %s; password %s " % (session["username"], session.get("password"))


@app.route("/getSession/<name>")
def getSession(name):
    return session[name]


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
