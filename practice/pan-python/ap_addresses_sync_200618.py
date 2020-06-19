import re
from lxml import etree
import subprocess
import requests


def getSynAddrDict():
    text = requests.get(
        "http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
    # itemLength = 63
    list01 = text.split("\n")
    returnDict = {}
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                if item == "null":
                    continue
                # print(type(item))
                if len(item) <= 63:
                    continue
                returnDict[item[:63:]] = item
    return returnDict

# print(getSynAddrDict())
# print(set(getSynAddrDict().keys()))


'''
def getSynAddrSet(isName=True):
    text = requests.get(
        "http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
    # itemLength = 63
    list01 = text.split("\n")
    returnList = []
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                if item == "null":
                    continue
                # print(type(item))
                if len(item) <= 63:
                    continue
                if isName:
                    returnList.append(item[:63:])
                else:
                    returnList.append(item)
    return set(returnList)
'''
# print(getSynList())

pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"


def getPaAddrDict():
    cmd = "panxapi.py -xs \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    # err = p.stderr.read()
    # print(out.decode("gbk"), type(out.decode("gbk")))

    xml = etree.fromstring(out.decode(
        'utf-8'), etree.XMLParser(remove_blank_text=True))
    b = xml.xpath(
        '//member[contains(text(),"insideIP") or contains(text(),"paupdate") or contains(text(),"outsideIP")]/../../@name')

    print(type(b), b, b[0])
    returnDict = {}
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
            returnDict[item] = address.text
    # print(returnDict)
    return returnDict


# getPaAddrDict()


# def getPaAddrSet():
#     cmd = "panxapi.py -xs \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""

#     p = subprocess.Popen(
#         cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     out = p.stdout.read()
#     # err = p.stderr.read()
#     # print(out.decode("gbk"), type(out.decode("gbk")))

#     xml = etree.fromstring(out.decode(
#         'utf-8'), etree.XMLParser(remove_blank_text=True))
#     returnList = xml.xpath(
#         '//member[contains(text(),"insideIP") or contains(text(),"paupdate") or contains(text(),"outsideIP")]/../../@name')

#     # print(type(returnList),returnList,returnList[0])
#     return set(returnList)

# print(__getPaAddressList())


# def wrapXml(name, address):
#     entry = etree.Element("entry", name=name)
#     tag = etree.SubElement(entry, "tag")
#     member = etree.SubElement(tag, "member")
#     member.text = "outsideIP"
#     if re.match(pattern, address):
#         ip_netmask = etree.SubElement(entry, "ip-netmask")
#         ip_netmask.text = address
#     else:
#         ip_netmask = etree.SubElement(entry, "fqdn")
#         ip_netmask.text = address

#     xml = etree.tostring(entry).decode("UTF-8")
#     return xml

def wrapXml(name, address):
    #print("\nname: %s \nip: %s \nnetmask: %s\n" %(name, ip, netmask))
     
    if re.match(pattern, address):
        returnStr = '\"<entry name=\'' +name+ '\'><ip-netmask>'+address+'</ip-netmask><tag><member>outsideIP</member></tag></entry>\"'
    else:
        returnStr = '\"<entry name=\'' +name+ '\'><fqdn>'+address+'</fqdn><tag><member>outsideIP</member></tag></entry>\"'
    return returnStr

def exeCmd(cmd):
    print(cmd)
    p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    print(out.decode("gbk"),err.decode("gbk"), type(out.decode("gbk")))

def delPaAddr():
    delPaAddrSet = getPaAddrDict().keys() - getSynAddrDict().keys()
    print(delPaAddrSet)
    for item in delPaAddrSet:
        # print("del", wrapXml(item, getPaAddrDict()[item]))
        # panxapi.py -dx "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='172.16.1.2']"
        cmd = "panxapi.py -dx \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name=\'"+item+"\']\""
        # print(cmd)
        exeCmd(cmd)
        return
    return

commit = "panxapi.py -C \"\" --sync"

# delPaAddr()

# exeCmd(commit)

def addPaAddr():
    addPaAddrSet = getSynAddrDict().keys() - getPaAddrDict().keys()
    print(addPaAddrSet, type(addPaAddrSet))
    addPaAddrSet = {}
    for item in addPaAddrSet:
        text = wrapXml(item, getSynAddrDict()[item])
        print("add", text)
        # panxapi.py -Sx "<entry name="'192.16.3.3'"><ip-netmask>255.255.255.0</ip-netmask></entry>" "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address"
        cmd = "panxapi.py -S " +text+" \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""
        print(cmd)
        # exeCmd(cmd)
        return
    return


addPaAddr()

# exeCmd(commit)


