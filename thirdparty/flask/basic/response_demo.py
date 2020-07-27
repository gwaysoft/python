from flask import Flask, make_response

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    # return response, status (or string), header (tuple or dictionary)
    # return ("success", 400, [("language", "java"), ("s", "python")])
    # return "success", 400, {"language": "java", "second": "javascript"}
    return "success", "400 error", {"language": "java", "second": "javascript"}


# make_response
@app.route("/res")
def res():
    print("res")
    resp = make_response("index 2")
    resp.status = "200 yes"
    resp.headers["language"] = "java"
    return resp


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
