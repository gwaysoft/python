#!/usr/bin/python3.6
import cx_Oracle

host = "172.16.7.232"  # 数据库ip
port = "1522"  # 端口
sid = "o232g4"  # 服务名
dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect("ebaotech_oa", "ebaotech_oapwd", dsn)


cursor = conn.cursor()
sql = "select * from fd_user where username in ('david.wei','silei.yang')"
cursor.execute(sql)
result = cursor.fetchall()
count = cursor.rowcount
print(" ===================== ")
print(" Total: ", count)
print(" ===================== ")
for row in result:
    print(row)
cursor.close()
conn.close()
