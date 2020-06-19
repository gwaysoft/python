def returnTuple():
    return 1, "eee", [1, 2, 3]

def returnNone():
    pass

# print(returnNone())
val = returnTuple()
print(val[0], type(val))



def moeny():
    list01 = []
    while True:
        try:
            inMoney = input("Please input money, q is exit: ")
            if inMoney == 'q':
                break
            inMoney = float(inMoney)
            list01.append(inMoney)
            pass
        except:
            print("Please input float, or q, except")
            pass
    return list01


def collectMoney(*inMoneys):
    print(inMoneys)

# collectMoney(*moeny())

msg = "ssss"
def scope():
    # global msg
    msg  = "222"
    print(msg)

# scope()
# print(msg)  

import math
result = lambda r:math.pi * r * r
# print(result(10))

bookInfo = [(1001, "飞行", 25, 75), (1002, "gooo", 43, 90), (1005, "gooo", 43, 77), (1003, "rooo",33, 60)]
print(type(bookInfo[1]), type(bookInfo))

bookInfo.sort(key=lambda x:(x[2], x[2]/x[3], x[0]))
print(bookInfo)
