import chardet, struct
f= open('bb',mode='rb')
data=f.read()
print(data)
struct.unpack('B', data)
print(data.decode('utf-8'))
f.close()
result=chardet.detect(open('bb',mode='rb').read())
print(result)