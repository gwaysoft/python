
import subprocess
from lxml import etree

cmd = "panxapi.py -xs \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""

p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out = p.stdout.read()
err = p.stderr.read()
# print(out.decode("gbk"), type(out.decode("gbk")))
# dict = json.loads(out.decode("gbk"))
# print(dict,dict["entry"], type(dict))
# print(out.decode("utf-8") == "")
# print(err.decode("gbk"))
# print(err.decode("utf-8"))



xml=etree.fromstring(out.decode('utf-8'), etree.XMLParser(remove_blank_text=True)) #初始化生成一个XPath解析对象
# result=etree.tostring(xml,encoding='utf-8')   #解析对象输出代码
# print(type(xml))
# print(type(result))
# print(result.decode('utf-8'))

# get all addresses
#b = xml.xpath('//ip-netmask/text()|//fqdn/text()|//ip-range/text()')

# get addresses by tag
#b = xml.xpath('//member[contains(text(),"insideIP") or contains(text(),"paupdate") or contains(text(),"outsideIP")]/../../@name')


b = xml.xpath('//member[contains(text(),"insideIP") or contains(text(),"paupdate") or contains(text(),"outsideIP")]/../../@name')

print(etree.tostring(xml.find(".//address/entry[@name='192.16.3.3']")))

# print(xml.find(".//address/entry[@name='192.16.3.3']/ip-netmask").text)
# print(xml.find(".//address/entry[@name='test tag']/ip-netmask").text)
# print(xml.find(".//address/entry[@name='taiping-ls-uat-oracle.cu2oqclywbho.ap-southeast-1.rds.amazonaws']/fqdn").text)

import re

pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
print(type(b),b,b[0])
dict01 = {}
for item in b:
    # print(item)
    if re.match(pattern, item):
        text = ".//address/entry[@name=\'"+item+"\']/ip-netmask"
    else:
        text = ".//address/entry[@name=\'"+item+"\']/fqdn"
    # print(text)
    address = xml.find(text)
    if address != None:
        print(address.text)
        dict01[item] = address.text
    

print(dict01)

print(type(b),b,b[0])






