from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_json", methods=["POST"])
def get_json():
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    print(data)
    name = ""
    if len(name):
        print("you")
    else:
        print("ee")
    # for k, v in data:
    #     if k == "name" and v is not None:
    #         name = v

    # jsonify: Content - Type: application / json
    return jsonify({'name': data["name"] + "dddd", 'age': data["age"] + 100})
    # json.dumps: Content-Type: text/html; charset=utf-8
    # return json.dumps({'name': name, 'age': age})


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
