from flask import Flask, jsonify, render_template, make_response, request, redirect, abort, session, url_for
# from werkzeug.contrib.fixers import ProxyFix\
from gspackage.logging.logger import logger
import business
import userManager
import json

app = Flask(__name__)
app.secret_key = "super secret key"
# app.config['SERVER_NAME'] = '172.18.5.22:8082'


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@app.route("/")
def index():
    logger.info("idnex")
    # with app_ctx:
    # userManager.update_token_by_name("dwdd","eqqee")
    # user = userManager.get_user_by_id(1)
    # logger.debug(user)
    # logger.debug(user.username)
    return render_template("index.html")
    # return "index"


@app.route("/login")
def login():
    # return render_template("http://www.baidu.com")
    # request.args.get("code")
    # resp = make_response(json_str)
    # resp.headers["Content-Type"] = "application/json"
    # resp.headers["dd"] = "dd"
    code = request.args.get("code")
    if code is None:
        abort(401)
    print("code: %s" % code)

    import requests
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'authorization_code', "code": code}
    # token = requests.post("http://172.30.2.115:8080/oa/oauth2/json/getToken.action",
    resultStr = requests.post("https://oa.ebaotech.com/oa/oauth2/json/getToken.action",
                              headers=headers, data=data).text

    logger.info(resultStr)
    if (resultStr is None) or (resultStr == "{}"):
        return "error"

    result = json.loads(resultStr)
    if result["username"] is None or result["token"] is None:
        return "error"
    userManager.update_token_by_name(result["username"], result["token"])
    # vue_url = "http://172.18.5.22:8082/layout/ddd" + result["token"]
    vue_url = "http://172.18.5.22:9528/#/layout/" + result["token"]
    reps = make_response(render_template("layout.html", vue_url=vue_url), "success")
    reps.delete_cookie("vue_admin_template_token")
    print(request.cookies.get("token"))
    reps.set_cookie("token1", result["token"])#, domain="172.18.5.22:8082", path="/")
    # return redirect("http://172.18.5.22:8082/layout/ddd" + result["token"])
    return reps


@app.route("/layout")
def layout():
    reps = make_response(render_template("layout.html", vue_url="http://172.18.5.22:8082/layout/ddd"), "success")
    reps.delete_cookie("vue_admin_template_token")
    print(request.cookies.get("cccc"))
    reps.set_cookie("cccc", "dddsssssddd")
    # return redirect("http://172.18.5.22:8082/layout/ddd" + result["token"])
    return reps


@app.route("/pa", methods=["GET"])
def pa():
    print("ddddddd:  " + session["username"])
    if session["username"] is None:
        abort(401)
    return render_template("pa.html", title="paloauto: synchronize addresses by awsprod")


@app.route("/business", methods=["POST"])
def put():
    print("dddddd:   " + session["username"])
    if session["username"] is None:
        abort(401)
    return render_template("business.html", title="Waiting 1 ~ 2 minutes, could not refresh the page")


@app.route("/api/company")
def company():
    if session["username"] is None:
        abort(401)
    # print(business.getSynAddrList())
    retList = business.job();

    rows = [{"action": "Add", "list": list(retList[0])},
            {"action": "Del", "list": list(retList[1])}]
    return jsonify(rows)


@app.route("/api/menu")
def menu():
    import json
    with open('dataList.json') as f:
        data = json.loads(f.read())
    print("ddd")
    return jsonify(data)


# app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    logger.info("startwwwwww")
    app.run(debug=True, host="0.0.0.0")
