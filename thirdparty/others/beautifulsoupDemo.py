# pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests
text = requests.get("http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
#print(text,type(text))

list01 = BeautifulSoup(text,"html.parser")
for item in list01:
    print(item,type(item))