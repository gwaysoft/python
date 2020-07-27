from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    reps = make_response("success")
    # default, When the browsing session ends
    reps.set_cookie("name", "python")
    reps.set_cookie("name1", "python1")
    reps.set_cookie("name2", "python2", max_age=3600)
    reps.headers["Set-Cookie"] = "name3=python3000; Path=/"
    return reps


@app.route("/getCookie/<name>")
def getCookie(name):
    c = request.cookies.get(name)
    return c


# created = expired
@app.route("/delCookie/<name>")
def delCookie(name):
    reps = make_response("success")
    reps.delete_cookie(name)
    return reps


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
