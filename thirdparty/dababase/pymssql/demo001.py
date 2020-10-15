import pymssql

conn = pymssql.connect(host='192.168.171.10',
                       user='door',
                       password='door2012',
                       database='agms60',
                       charset='utf8')

# 查看连接是否成功
cursor = conn.cursor()
sql = 'select * from staff'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()

print(rs)