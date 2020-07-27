from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# step 1, define  converter
class MobileConverter(BaseConverter):
    """"""

    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'

    # after converter, transfer from @app.route("/send/<re:mobile>") to def send(mobile)
    def to_python(self, value):
        print(self.__class__, value)
        return value

    # to be executed, at invoke url_for
    def to_url(self, value):
        print(self.__class__, value)
        return value


# step 2, add converter to flask
app.url_map.converters["re"] = MobileConverter


# converter
@app.route("/send/<re:mobile>")
def send(mobile):
    return "send sms to %s" % mobile

@app.route("/")
def index():
    # /send/18912345678
    url = url_for("send", mobile="18912345678")
    return redirect(url)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host="192.168.2.110", port=5000)
    # app.run(debug=True)
