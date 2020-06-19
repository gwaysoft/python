from flask import Flask

app = Flask(__name__)


@app.route('/demo', methods=['GET'])
def demo():
    return "gunicorn and flask demo."

# gunicorn -w 4 -c config_demo.py myapp:app
# netstat -lnp|grep 18000