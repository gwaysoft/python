# t = ("33",)
# print(type(t))
# t = ("33")
# print(type(t))
def returnEmptyTuple():
    return ()

# print(returnEmptyTuple())  
# print(tuple(range(2,21,2)))  
# print(list(range(2,21,2)))

t01 = tuple(range(2,21,2))

t01 = t01 + (33,)
print(type(t01), type(str(t01)))

t02 = eval(str(t01))
# print(t02, type(t02))
# print(t01[0:2])
# for item in t01:
#     print(item, end=" | ")

# for index, item in enumerate(t01):
#     if index%2 ==0:
#         print("%d \t %d" %(index,item), end= "\t | \t")
#     else:
#         print("%d \t %d \n" %(index,item))

import random
print(tuple(random.randint(10,20) for i in range(10)))

t03 = (random.randint(10,20) for i in range(10))
print(type(t03), tuple(t03))