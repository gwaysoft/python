from flask import Flask, jsonify, render_template
# from werkzeug.contrib.fixers import ProxyFix
import business

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="paloauto: synchronize addresses by awsprod")


@app.route("/business", methods=["POST"])
def put():
    print("business")
    return render_template("business.html", title="Waiting 1 ~ 2 minutes, could not refresh the page")


@app.route("/api/company")
def company():
    # print(business.getSynAddrList())
    retList = business.job();

    rows = [{"action": "Add", "list": list(retList[0])},
            {"action": "Del", "list": list(retList[1])}]
    return jsonify(rows)

# app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
