import pymysql

conn = pymysql.connect(
    host="192.168.2.110",
    user='root',
    password='123456',
    database='mysql_db',
    charset='utf8'
)

cursor_test = conn.cursor()

sql = '''insert into user (username, age) values ('gade', 21)'''

try:
    cursor_test.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()
