# rr="rr"
# list01 = [23, "wod", (2,"aa"),[2,"aa"],{"you":55, "i":44,"you":rr}, "wod","wod"]
templist = ["Dynamic address groups in vsys vsys1:",
            "----------------------------------------------------",
            "",
            "----------------defined in vsys --------------------",
            "----------------defined in shared-------------------",
            "O: address object; R: registered ip; D: dynamic group; S: static group"]
print("%s %s" % (len(templist), str(templist)))
# print(list01.count("wod"))
# print(list01.index((2,"aa")))

listInt = [12, 300, 2, 4, 78, 33]
list03 = [round(i * 0.2, 0) for i in listInt if i > 10]
print("%s %s" % (len(list03), str(list03)))
# print(sum(listInt, 10000))

# listInt.sort(reverse=True)
# print(listInt)

listChange = sorted(listInt, reverse=False)


# print(listChange)
# print(listInt)

# def defaultParam(first="33", second=2):
#     print(first, second)

# defaultParam(second="hao", first=3)    

# print(isinstance(list01,list))
def forFor(listFor):
    if isinstance(listFor, list):
        for item in listFor:
            if isinstance(item, list):
                forFor(item)
            else:
                print(item)


# forFor(list01)

# for idx, item in enumerate(list01):
#     if idx%2 == 0:
#         print(str(item) + "\t\t", end="")
#     else:
#         print(str(item) + "\n")

# list01.append("dd")
# list01.insert(0, "first")
# list01.extend([8,5])
# del list01[-1]
# list01.remove(8)
# if "dd" in list01:
#     list01.remove("dd")
# print(len(list01), list01)
# import datetime
# weekday = datetime.datetime.now().weekday()
# print(weekday)

# list02 = list(range(2, 21, 2))
# print(list02)
# string = "几位集团"
# print(list(string))

# del list02
# NameError: name 'list02' is not defined
# print(list02)

import random

list03 = [random.randint(10, 100) for i in range(10)]

list04 = [1, 1, 1, 1]
print(list04)

# filter redundancy
print(list(set(list04)))
