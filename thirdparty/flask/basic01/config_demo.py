from flask import Flask, current_app

# create falsk app object
# __name__ is current module (file) name
# Flask(__name__) current module (file) directory as work directory
# |-static as default static directory
# |-templates as default template directory
app = Flask(__name__,
            static_url_path="/",
            static_folder="static",  # default is static
            template_folder="templates"  # default is templates
            )


class Config(object):
    DEBUG = True
    PY = "python"
    YY = "eeee"


app.config.from_object(Config)


# 定义视图函数
@app.route("/config")
def index():
    # appconfig = app.config["YY"]
    appconfig = current_app.config.get("YY")
    return "hello flask" + str(appconfig)


if __name__ == '__main__':
    # app.run() 简易的测试服务器
    # 启动flask
    # host default 127.0.0.1
    # port 5000
    app.run(debug=True, host="192.168.2.110")
