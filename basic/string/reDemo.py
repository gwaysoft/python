import re

# pattern = r"(黑客)|(抓包)|(监听)"
# str = "我是一名程序员，黑2客，不错的"
# match = re.search(pattern, str)

# if match == None:
#     print("security")
# else:
#     print("risk")

# pattern = r"(黑客)|(抓包)|(监听)"
# str = "我是一名程序员，黑客，不错的"
# repStr = "红"
# match = re.sub(pattern, repStr, str)
# print(match)


# pattern = r"mr_\w"
# str = "dddMR_shop mr_shop mR_shop"
# match = re.findall(pattern, str, re.I)
# print(match)
# match = re.search(pattern, str, re.I)
# print(type(match.start()),match)
# print("{:d},{:d},{:s}".format(match.start(), match.end(),match.group()))

# pattern = r"(13[568]\d{8})|(15[1289]\d{8})$"
# number = "13523040204 13523040203"
# match = re.match(pattern, number)
# print(type(match),match)
# if match == None:
#     print("Invalid")
# else:
#     print("Valid")

pattern = r"[,|?|&]"

url = "http://www.baidu.com?ee=22&xx=3333xxx"

match = re.split(pattern,url)
print(match)