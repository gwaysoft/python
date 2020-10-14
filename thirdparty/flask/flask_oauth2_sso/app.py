from flask import Flask, render_template, request, redirect, abort, session, url_for
# from werkzeug.contrib.fixers import ProxyFix\
import json

app = Flask(__name__)
app.secret_key = "super secret key"

# client_id = 'ts'
# redirect_uri = "172.25.10.24:5000/login"
client_id = 'pa'
redirect_uri = "192.168.2.110:5000/login"


@app.route("/")
def index():
    vue_url = "https://oa.ebaotech.com/oa/oauth2.action?client_id=" + client_id + "&response_type=code&redirect_uri=" + redirect_uri
    return render_template("index.html", vue_url=vue_url)


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
    resultStr = requests.post("https://oa.ebaotech.com/oa/oauth2/json/getToken.action",
                              headers=headers, data=data).text

    if (resultStr is None) or (resultStr == "{}"):
        return "error"

    result = json.loads(resultStr)
    if result["username"] is None or result["token"] is None:
        return "error"

    vue_url = "http://172.16.0.39:9528/#/layout/" + result["token"]
    # vue_url = "http://172.18.5.48:9528/#/layout/" + result["token"]
    # vue_url = "http://172.18.5.22:9528/#/layout/" + result["token"]
    return render_template("redirect.html", vue_url=vue_url)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
