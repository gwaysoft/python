from flask import Flask, abort, Response

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    # abort(Response("error"))
    abort(404)
    return "success"

@app.errorhandler(404)
def handle_404_error(error):
    return "handle_404_error <br> %s" % error


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
