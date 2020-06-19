# pip install requests
import requests


text = requests.get("http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text

list01 = text.split("\n")
list02 = []
for line in list01:
    if line.find(",") != -1:
        lineList = line.split(",")
        for item in lineList:
            if item == "null":
                continue
            list02.append(item)

print(list02)