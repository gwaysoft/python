from flask import Flask
import UserManager

app = Flask(__name__)



@app.route("/")
def index():
    user = UserManager.get_user(3)
    print(user)
    return "index"


if __name__ == '__main__':
    app.run(debug=True, host="192.168.2.110")
