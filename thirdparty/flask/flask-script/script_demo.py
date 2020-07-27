# pip install flask-script
# usage 1. python script_demo.py runserver --host 0.0.0.0 -D
# usage 2. python script_demo.py shell
from flask_script import Manager
from flask import Flask

app = Flask(__name__)

manager = Manager(app)

@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    # app.run(debug=True, host="192.168.2.110")
    manager.run()