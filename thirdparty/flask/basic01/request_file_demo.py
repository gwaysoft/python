from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file_name")
    if file is None:
        return "None file"
    localfile = open("demo.png", "wb")
    data = file.read()
    localfile.write(data)
    localfile.close()
    return "success"

@app.route("/upload_flask", methods=["POST"])
def upload_flask():
    file = request.files.get("file_name")
    if file is None:
        return "None file"
    file.save("demo_flask.png")
    return "success"


if __name__ == "__main__":
    app.run(debug=True, host="192.168.2.110")
