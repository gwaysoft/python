
# panxapi.py after command must be double quotation marks
import subprocess
from lxml import etree

# cmd = "panxapi.py -xs \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group\""
cmd = "panxapi.py -xs \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""


p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out = p.stdout.read()
err = p.stderr.read()
print(out.decode("gbk"), type(out.decode("gbk")))
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


# b = xml.xpath('//entry/tag[member="paupdate"]/../@name')
b = xml.xpath('//entry/tag[member="paupdate"]/../@name')
print(type(b),b,b[0])

# b = xml.xpath('//entry[@name="tagTestGroup"]//text()')
# print(type(b),b,b[0])



