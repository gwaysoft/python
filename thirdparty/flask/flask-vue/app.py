import sqlite3
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pa.html", title="vue flask")


@app.route("/api/company")
def company():
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = "select * from company"
    rows = cur.execute(sql).fetchall()
    rows = [dict(row) for row in rows]
    return jsonify(rows)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
