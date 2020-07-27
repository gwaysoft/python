str = "我的typython,ggo各个"
# print(str.count("t",0,10))
# print(str.rfind("y"))
print(str.find("y"))
# print("h" in str)
# print(str.index("y"))
# print(str.rindex("y"))
print(str[:3])
# print(type(str.encode()))
# print(len("我的".encode()))
# print(len("我的".encode("GBK")))
# str = '37028320190202219'
# try:
#     print(str[6:10],'year',str[10:12],'month', str[12:14],'day')


# except IndexError:
#     print("index Error")

# str = '收藏、投币、点赞即'
# list01 = str.split("、")
# print(type(list01))
# print("$" + "$".join(list01))

# str = '''s
#     sfs ewer
#     ese         eex     
#     d       
#     s'''
# print(str.strip("s"))
# print(str)

# templates = "NO. %09d\t name: %s\t url: https://www.%s.com"
# template01 = "NO. {:0>9s}\t name: {:s}\t url: https://www.{:s}.com"
# item = (7, "百度", "baidu")
# print(templates%item)
# print(template01.format("7", "百度", "baidu"))

# template01 = "NO. {0:0>9s}\t name: {1:s}\t url: https://www.{2:s}.com"
# print(template01.format("7", "百度", "baidu"))

# str = "-+0m.n"
# list01 = list(str)
# str = "[" + "][".join(list01) +"]"
# print(str)

# import math
# print("${:,.2f}".format(23333+22222))
# print("{0:,.1f}  {0:E}".format(2123455.3))
# print("{0:.5f}\t{1:#x}".format(math.pi,100))
# print("{:.0%}".format(0.99))