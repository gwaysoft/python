from flask import Flask

app = Flask(__name__,
            static_url_path="/",
            static_folder="static",  # default is static
            template_folder="templates"  # default is templates
            )


@app.route("/")
def index():
    return "hello flask"


@app.route("/get", methods=["GET", "POST"])
@app.route("/get1")
def get():
    return "hello flask get"


if __name__ == '__main__':
    print(app.url_map)
    # app.run(debug=True, host="192.168.2.110", port=5000)
    app.run()
