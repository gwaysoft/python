from flask import Flask, redirect, url_for

# create falsk app object
# __name__ is current module name
# Flask(__name__) current module directory as work directory
# |-static as static directory
# |-templates as templates directory
app = Flask(__name__)


# 定义视图函数
@app.route("/")
def index():
    return "hello flask"


if __name__ == '__main__':
    # app.run() 简易的测试服务器
    # 启动flask
    app.run(debug=True, host="192.168.2.110")


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
