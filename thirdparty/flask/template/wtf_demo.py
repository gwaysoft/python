from flask import Flask, render_template, redirect, url_for, session
# pip install flask-wft
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

# CSFR
app.config["SECRET_KEY"] = "sdfsssssdwasdfasdfadsfs"


# define form class
class RegisterForm(FlaskForm):
    user_name = StringField(label="Username", validators=[DataRequired("Username is not none")])
    password1 = PasswordField(label="Password1", validators=[DataRequired("Password is not none")])
    password2 = PasswordField       (label="Password2",
                              validators=[DataRequired("Password is not none"), EqualTo("password1", "不一致")])
    submit = SubmitField(label="Submit")


@app.route("/reg", methods=["POST", "GET"])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        print("validate go")
        user_name = form.user_name.data
        password1 = form.password1.data
        password2 = form.password2.data
        print(user_name, password1, password2)
        session["user_name"] = user_name
        return redirect(url_for("index"))
    else:
        print("not go")

    return render_template("reg.html", form=form)


@app.route("/")
def index():
    user_name = session.get("user_name")
    return "index %s" % (user_name)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
