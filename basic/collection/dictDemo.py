dict01 = {"aaa":22, "bbb":"33","bbb":"33"}
print(dict01, type(dict01), str(len(dict01)))

key = ["aaa", "bbb", "ccc"]
value = ["33", 1212, ["eee",]]


print({k:v for k, v in zip(key,value)})

# dict01 =  zip(key,value)
# print(dict(dict01))

# key = ("aaa", "bbb", "ccc")
# value = ["33", 1212, ["eee",]]
# dict01 = {key: value}
# print(dict01)

# dict01 =  zip(key,value)
# print(dict(dict01))

# dict01 = dict(aaa=22, bb ="3")

# dict01["last"] = "last"

# print(dict01)

# del dict01["bb"]



# print(dict01.items())
# print(dict01.keys())
# print(dict01.values())

# for k, v in dict01.items():
#     print(k,v)

# print(dict01)

# print(dict01["a"] if "a" in dict01 else "none")
# print(dict01.get("a", "3"))

# key = ("aaa", "bbb", "ccc")
# dict02 = dict.fromkeys(key)
# print(dict02)

import random
dict03 = {i: random.randint(10,100) for i in range(10)}
dict03[1]=10
dict03[100]=100
print(dict03.keys(),dict03.values(),len(dict03), type(set(dict03.keys())))
