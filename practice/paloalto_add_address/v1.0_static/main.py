from gspackage import comparison, config
from gspackage import gsLogger

logger = gsLogger.getLogger(logDir="paloalto_address", fileName="address.log")

TAG = " tag " + config.getValue(key="tag")
OPERATOR_SET = "set address "
OPERATOR_DELETE = "delete address "
URL_SYN = config.getValue(key="url")


def getSynAddrList():
    import requests
    text = requests.get(URL_SYN).text
    # itemLength = 63
    list01 = text.split("\n")
    returnList = []
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                if item == "null":
                    continue
                returnList.append(item)
    returnList.append("122.122.122.2")
    return returnList


def wrapItemList(addList, delList, tag):
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


def resetAddrList(config_commands):
    if len(config_commands) == 0:
        return
    config_commands.append("commit")
    print(config_commands)

    from netmiko.paloalto import PaloAltoPanosSSH
    connectConfig = {
        'device_type': 'paloalto_panos',
        'host': '172.16.8.81',
        'username': 'python-api',
        'password': 'python'
    }

    net_connect = PaloAltoPanosSSH(**connectConfig)

    output = net_connect.send_config_set(config_commands)
    print(output)


def job():
    logger.debug("job start")
    addrList = getSynAddrList();
    print(addrList)
    addList = comparison.getAddItems(items=set(addrList))

    delList = comparison.getDelItems(items=set(addrList))
    operateList = wrapItemList(addList, delList, TAG);
    if len(operateList) == 0:
        return
    resetAddrList(operateList)

    # print(addList)
    # print(delList)
    comparison.resetItemList(items=set(addrList))

    logger.info("[ADD] total %s | add addresses: %s" % (len(addList), str(addList)))
    logger.info("[DEL] total %s | del addresses: %s" % (len(delList), str(delList)))


def scheduleJob(job):
    from apscheduler.schedulers.blocking import BlockingScheduler

    # BlockingScheduler
    scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'interval', seconds=30)
    # scheduler.add_job(job, 'interval', hours=6)
    scheduler.add_job(job, 'interval', minutes=2)
    # scheduler.add_job(job, 'cron', second=15)
    # nohup python3 -u business01.py > test.log 2>&1 &
    scheduler.start()


def main():
    logger.info("start")
    job()
    # scheduleJob(job)
    # print(getSynAddrList())

    # print(getSynAddrList())
    # addAddress(getSynAddrList())
    # addAddress(delSynAddrList())


if __name__ == "__main__":
    main()
