def filterChar(str):
    import re
    pattern = r'(one)|(1)|(一)'
    sub = re.sub(pattern, "@@", str)
    print(sub)

#filterChar("weew1sdfds一werwef")

def empty():
    pass

def weekFun():
    list01 = ['w01',
    'w02',
    'w03',
    'w04',
    'w05',
    'w06',
    'w07']
    print(list01)
    import datetime
    date = datetime.datetime.now().weekday()
    return list01[date]

# print(weekFun())

# default parameter is at last order
def position(p1, p2, p3="d p3", p4="default p4"):
    print("p1:%s, p2:%s, p3:%s, p4:%s" %(p1, p2, p3, p4))

# position(p2="p2", p1="p1")
# print(position.__defaults__)
# position(p2="p2", p3="p3", p1="p1", p4="p4")

def demo(obj=None):
    if obj == None:
        obj = []
    print(obj)
    obj.append(100)

# demo()
# demo()
# demo([1,2,3])

def coffee(*coffeeName):
    for item in coffeeName:
        print(item)

# coffee("a")
# coffee("a", "b", "c")
# list01 = ["a", "b", "c"]
# coffee(list01)
# coffee(*list01)

def sign(**sign):
    for k, v in sign.items():
        print(k, v)

sign(ab="33", bb="cc")
dic = {"ab":"33","bb":"cc"}
sign(**dic)
