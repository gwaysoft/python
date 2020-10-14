import myLogger

logger = myLogger.getLogger()

import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
COMPARISON_FILE = CURRENT_DIR + '/comparison.ini'


def getDomainsList(fileName):
    retList = []
    import re
    regular = re.compile('[^\s]*[.com|.cn]')
    i = 1
    with open(CURRENT_DIR + "/" + fileName, mode="r") as f:
        retList = re.findall(regular, f.read())
    return set(retList)


# print(len(getDomainsList("domains.ini")), getDomainsList("domains.ini"))

def getDomainIpList(domainList):
    logger.debug(str(len(domainList)) + " " + str(domainList))
    import socket
    retDict = {}
    errList = []
    for domain in domainList:
        # logger.debug(type(domain))
        try:
            ip = socket.gethostbyname(domain)
            retDict[ip] = domain
        except:
            errList.append(domain)
    if len(errList) > 0:
        logger.error(errList)
        from gspackage.utils.smtp import sendEmails
        logger.info(
            sendEmails(receivers=["vickor.zhang@ebaotech.com", "david.wei@ebaotech.com"], subject="Error Domain(s)",
                       content=str(errList)))
    return retDict


def addIpListToCisco(addIpList, cisco_ip):
    logger.debug("addIpList: " + str(addIpList))
    config_commands = ['ip access-list extended VM']

    addIpCmdHeader = "permit ip any host "

    for ip in addIpList:
        config_commands.append(addIpCmdHeader + ip)
    logger.debug(config_commands)

    from netmiko import ConnectHandler

    connectConfig = {
        'device_type': 'cisco_ios',
        'host': cisco_ip,
        'username': 'networkconfig',
        'password': 'Ebaotech2020'
    }
    net_connect = ConnectHandler(**connectConfig)
    output = net_connect.send_config_set(config_commands)
    logger.debug(output)

    output = net_connect.send_command("wr")
    logger.debug(output)

    for ip in addIpList:
        output = net_connect.send_command("sh startup-config | inc any host " + ip)
        logger.info(cisco_ip + " " + output)


def getUpdateIpList(retDict):
    logger.debug(str(len(retDict)) + " " + str(retDict))
    if len(retDict) == 0:
        return []
    import configparser
    config = configparser.ConfigParser()
    config.read(COMPARISON_FILE)

    # logger.debug("existedList: " + str(existedList))
    existedList = config["DEFAULT"].keys()

    addIpList = list(set(retDict.keys()).difference(set(existedList)))

    if len(addIpList) == 0:
        logger.debug("Not changes, thanks.")
        return addIpList

    addIpListToCisco(addIpList, "172.16.30.250")
    addIpListToCisco(addIpList, "172.16.30.251")

    for ip in addIpList:
        print("ip: %s; demain: %s " % (ip, retDict[ip]))
        config["DEFAULT"][ip] = retDict[ip]
    with open(COMPARISON_FILE, 'w') as fp:
        config.write(fp)
    return addIpList


def job():
    print(getUpdateIpList(getDomainIpList(getDomainsList("domains.ini"))))


def scheduleJob(job):
    from apscheduler.schedulers.blocking import BlockingScheduler

    # BlockingScheduler
    scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'interval', seconds=30)
    scheduler.add_job(job, 'interval', minutes=10)
    # scheduler.add_job(job, 'cron', second=15)
    # nohup python3 -u business01.py > test.log 2>&1 &
    scheduler.start()


def main():
    # print(getDomainIpList(getDomainsList("domains.ini")))
    # scheduleJob(job)
    job()
    pass


if __name__ == "__main__":
    main()
