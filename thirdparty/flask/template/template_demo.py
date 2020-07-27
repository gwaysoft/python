from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="python", age=18)


@app.route("/data")
def data01():
    data = {
        "name": "ss",
        "age": 18,
        "my_dict": {"city": "sh"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0,
    }

    request.data = "ddd"
    # resp = make_response(render_template("data.html", **data))
    # resp.status = "200 yes"
    # resp.headers["language"] = "java"
    return render_template("data.html", **data)


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")
    return render_template("xss.html", text=text)


# ----filter 1------------
# {{list | step2}}
def list_step_2(li):
    return li[::2]


app.add_template_filter(list_step_2, "step2")


# -----filter 2------------
@app.template_filter("step2_2")
def list_step_22(li):
    return li[::2]


if __name__ == '__main__':
    app.run(debug=True, host="192.168.2.110")
