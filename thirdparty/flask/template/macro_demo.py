from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("macro.html", type="text", value="from endpoint")


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host="0.0.0.0")
