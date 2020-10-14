import time
import redis
from flask import Flask

app = Flask(__name__)
# docker network create
# at the same network
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def get_user():
    import pymysql
    conn = pymysql.connect(
        host="db",
        user='root',
        password='123456',
        database='mysql_db',
        charset='utf8'
    )

    cursor_test = conn.cursor()

    sql = '''select * from user'''
    returnList = []
    try:
        cursor_test.execute(sql)
        result = cursor_test.fetchall()
        for row in result:
            print("username %s, age %s" % (row[0], row[1]))
            returnList = row
        conn.commit()
    except:
        conn.rollback()

    conn.close()
    return returnList

@app.route('/')
def hello():
    count = get_hit_count()
    return str(get_user()) + ' Hello World 23! I have been seen {} times.\n'.format(count)
