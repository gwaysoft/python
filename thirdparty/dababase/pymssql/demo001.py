import pymssql

conn = pymssql.connect(host='172.16.31.201',
                       user='sa',
                       password='eBao2014',
                       database='spiratest',
                       charset='utf8')


# 查看连接是否成功
cursor = conn.cursor()
sql = 'select * from user'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()

print(rs)