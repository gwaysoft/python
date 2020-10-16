#!/usr/bin/python3.6
import cx_Oracle

host = "172.17.1.163"  # 数据库ip
port = "1522"  # 端口
sid = "o163g4"  # 服务名
dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect("PAL_DEV", "PAL_DEVpwd", dsn)


cursor = conn.cursor()
sql = "select * from fd_user"
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
