from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    # 1 / 0
    return "index initialize response"


@app.route("/hello")
def hello():
    return "hello"


@app.before_first_request
def handle_before_first_request():
    print("handle_before_first_request")


@app.before_request
def handle_before_request():
    print(url_for("hello"), request.path, type(request.path), type(url_for("hello")))
    path = request.path
    if path == url_for("index"):
        print("index")
    elif path == url_for("hello"):
        print("hello")
    print("handle_before_request")


@app.after_request
def handle_after_request(response):
    print("handle_after_request")
    return response


# app.run(debug=True) teardown_request does not execute
@app.teardown_request
def handle_teardown_request(response):
    print("handle_teardown_request")
    return response


if __name__ == '__main__':
    app.run(debug=True, host="192.168.2.110")
