import pymssql

conn = pymssql.connect(host='172.16.31.201',
                       user='sa',
                       password='eBao2014',
                       database='spiratest',
                       charset='utf8', port='1433', as_dict=False)


# 查看连接是否成功
cursor = conn.cursor()
sql = 'select * from TST_USER'
# sql = 'select * from TST_PROJECT'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()

print(rs)