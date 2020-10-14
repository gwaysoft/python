import pymysql

conn = pymysql.connect(
    host="192.168.2.110",
    user='root',
    password='123456',
    database='mysql_db',
    charset='utf8'
)

cursor_test = conn.cursor()

sql = '''select * from user'''

try:
    cursor_test.execute(sql)
    result = cursor_test.fetchall()
    for row in result:
        print("username %s, age %s" % (row[0], row[1]))
    conn.commit()
except:
    conn.rollback()

conn.close()
