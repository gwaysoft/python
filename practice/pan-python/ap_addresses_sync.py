import re
from lxml import etree
import subprocess
import requests
import os
import logging
    

def getLogger(level):

    from logging.handlers import TimedRotatingFileHandler
    # formatter
    fmt = "%(levelname)s - %(asctime)s  - %(funcName)s - %(message)s"
    dateFmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=fmt, datefmt=dateFmt)

    # handler
    # when="D" day "W0" sunday
    # backupCount = 30 30天 保留时间
    # print(os.getcwd())
    handler = TimedRotatingFileHandler("./ap_sync.log", when="D",backupCount=30)
    handler.setFormatter(formatter)

    # handler
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)


    # logger
    logger = logging.getLogger("time")
    logger.addHandler(handler)
    logger.addHandler(streamHandler)
    logger.setLevel(level)
    return logger

logger = getLogger(logging.DEBUG)

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

    # print(type(b), b, b[0])
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
            # print(address.text)
            returnDict[item] = address.text
    # logger.debug(returnDict)
    return returnDict


# getPaAddrDict()

def wrapXml(name, address):
    #print("\nname: %s \nip: %s \nnetmask: %s\n" %(name, ip, netmask))
     
    if re.match(pattern, address):
        returnStr = '\"<entry name=\'' +name+ '\'><ip-netmask>'+address+'</ip-netmask><tag><member>outsideIP</member></tag></entry>\"'
    else:
        returnStr = '\"<entry name=\'' +name+ '\'><fqdn>'+address+'</fqdn><tag><member>outsideIP</member></tag></entry>\"'
    return returnStr

def exeCmd(cmd):
    logger.debug(cmd)
    p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    logger.debug(out.decode("gbk"))
    logger.debug(err.decode("gbk"))

def delPaAddr():
    delPaAddrSet = getPaAddrDict().keys() - getSynAddrDict().keys()
    logger.debug(delPaAddrSet)
    for item in delPaAddrSet:
        # print("del", wrapXml(item, getPaAddrDict()[item]))
        cmd = "panxapi.py -dx \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name=\'"+item+"\']\""
        logger.info("del - \t" + item)
        # exeCmd(cmd)
        return
    return




# delPaAddr()

# exeCmd(commit)

def addPaAddr():
    addPaAddrSet = getSynAddrDict().keys() - getPaAddrDict().keys()
    # print(addPaAddrSet, type(addPaAddrSet))
    # addPaAddrSet = {}
    for item in addPaAddrSet:
        text = wrapXml(item, getSynAddrDict()[item])
        # print("add", text)
        # panxapi.py -Sx "<entry name="'192.16.3.3'"><ip-netmask>255.255.255.0</ip-netmask></entry>" "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address"
        cmd = "panxapi.py -S " +text+" \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""
        logger.info("add -\t" + item)
        # exeCmd(cmd)
        return
    return


commit = "panxapi.py -C \"\" --sync"


def main():
    addPaAddr()
    
    # exeCmd(commit)


if __name__ == '__main__':
    main()
    pass


