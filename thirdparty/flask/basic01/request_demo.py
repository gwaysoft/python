from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    # name1, name2 = request.form.get("name", "default"), request.form["name"]
    # print("%s" % request.data.decode("utf-8"))
    abort(Response("error"))
    abort(500)
    name = request.form.get("name")
    print(request.args.get("arg1"))
    print(str(request.form.getlist("name")))
    print(request.args.getlist("arg1"))
    print(request.headers)
    print(request.method)
    return "name %s" % (name)


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
