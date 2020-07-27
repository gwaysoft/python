from flask import Flask, flash, render_template

app = Flask(__name__)

# use session
app.config["SECRET_KEY"] = "sdfsssssdwasdfasdfadsf"

flag = True


@app.route("/")
def index():
    global flag
    if flag:
        flash("ddd")
        flash("ddwwwwwwd")
        flag = False
    return render_template("flash.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
