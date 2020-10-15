import pymysql

conn = pymysql.connect(
    host="192.168.2.110",
    user='root',
    password='123456',
    database='mysql_db',
    charset='utf8'
)

cursor_test = conn.cursor()

cursor_test.execute("drop table if exists user")

sql = '''create table user(
    username char(20),
    age int)'''

cursor_test.execute(sql)
conn.close()
