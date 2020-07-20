from flask import Flask

app = Flask(__name__,
            static_url_path="/",
            static_folder="static",  # default is static
            template_folder="templates"  # default is templates
            )


# converter 转换器 -> int
@app.route("/goods/<int:goods_id>", methods=["GET", "POST"])
def goods_id(goods_id):
    return "googid: " + str(goods_id)


# default string, excluding /
@app.route("/goodsName/<goods_name>", methods=["GET", "POST"])
def goods_name(goods_name):
    return "googName: " + str(goods_name)


if __name__ == '__main__':
    print(app.url_map)
    # app.run(debug=True, host="192.168.2.110", port=5000)
    app.run(debug=True)
