from gspackage import config
from gspackage import gsLogger, paloauto
import logging


logger = gsLogger.getMyLogger(logDir="paloalto_address", fileName="address.log")
# logger = gsLogger.getMyLogger(logDir="paloalto_address", fileName="address.log", fileLevel=logging.DEBUG)

TAG = " tag " + config.getValue(key="tag")
# TAG = " tag cloud-env"
OPERATOR_SET = "set address "
OPERATOR_DELETE = "delete address "
URL_SYN = config.getValue(key="url")
PA_CMD_GET_ADDR_TAG = "show object dynamic-address-group name " + config.getValue(key="tag")
TEST_IP = config.getValue(key="test_ip")


def getPAAddrListByTag(command):
    output = paloauto.executeCommand(command)
    outList = output.split("\n")
    tagList = []
    for item in outList:
        if item.find("(O)") == -1:
            continue
        tagList.append(item.strip().replace(" (O)", ""))
    return tagList


def getSynAddrList():
    import requests
    text = requests.get(URL_SYN).text
    # itemLength = 63
    list01 = text.split("\n")
    returnNameList = []
    returnSourceDict = {}
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                if item == "null":
                    continue
                name = item[:63:]
                returnNameList.append(name)
                returnSourceDict[name] = item
    returnNameList.append(TEST_IP)
    returnSourceDict[TEST_IP] = TEST_IP
    return returnNameList, returnSourceDict


def wrapItemList(addList, delList, tag):
    logger.debug(addList)
    logger.debug(delList)
    returnList = []
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    for item in addList:
        import re
        if re.match(pattern, item):
            # continue
            text = OPERATOR_SET + item[:63:] + tag + " ip-netmask " + item
        else:
            # if len(item) >= 63:
            text = OPERATOR_SET + item[:63:] + tag + " fqdn " + item
        returnList.append(text)

    for item in delList:
        text = OPERATOR_DELETE + item[:63:]
        returnList.append(text)
    return returnList


def job():
    logger.debug("job start")
    paList = set(getPAAddrListByTag(PA_CMD_GET_ADDR_TAG))
    synNameList = set(getSynAddrList()[0]);
    addList = synNameList - paList
    delList = paList - synNameList
    print(delList,addList)
    addSourceList = []
    for item in addList:
        addSourceList.append(getSynAddrList()[1][item])
    # addList = ["122.122.122.11"]
    # delList = set(getPAAddrListByTag("show object dynamic-address-group name cloud-env")) - set(getPAAddrListByTag(
    #     "show object dynamic-address-group name awsprod"))
    operateList = wrapItemList(addSourceList, delList, TAG);
    logger.debug(operateList)
    if len(operateList) == 0:
        logger.info("Nothing to update, thanks.")
        return [], []
    # execute config command
    logger.debug(paloauto.executeConfigCommand(operateList))
    logger.info("[ADD] total %s | add addresses: %s" % (len(addList), str(addList)))
    logger.info("[DEL] total %s | del addresses: %s" % (len(delList), str(delList)))
    return addList, delList


def main():
    logger.info("start")
    job()
    logger.info("end")


if __name__ == "__main__":
    main()
