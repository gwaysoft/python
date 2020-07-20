from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# step 1, define  converter
class RegexConverter(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        # super().__init__(url_map)
        # print(regex)
        self.regex = regex


# step 2, add converter to flask
app.url_map.converters["re"] = RegexConverter


# converter
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send(mobile):
    return "send sms to %s" % mobile


if __name__ == '__main__':
    print(app.url_map)
    # app.run(debug=True, host="192.168.2.110", port=5000)
    app.run(debug=True)
