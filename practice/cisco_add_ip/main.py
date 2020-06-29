import myLogger

logger = myLogger.getLogger()


def getItemList(fileName):
    import configparser
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(fileName)

    keys = config["default"].keys()
    return list(keys), config


def getDomainIpList(domainList):
    import socket
    retList = []
    logger.debug("domainList: " + str(domainList))
    for domain in domainList:
        # logger.debug(type(domain))
        ip = socket.gethostbyname(domain)
        retList.append(ip)
    return retList


def addIpListToCisco(addIpList):
    logger.debug("addIpList: " + str(addIpList))
    config_commands = ['ip access-list extended VM']

    addIpCmdHeader = "permit ip any host "

    for ip in addIpList:
        config_commands.append(addIpCmdHeader + ip)
    logger.debug(config_commands)

    from netmiko import ConnectHandler

    connectConfig = {
        'device_type': 'cisco_ios',
        'host': '172.16.30.250',
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
        logger.info(output)


def getUpdateIpList(ipList):
    existedList, config = getItemList("novalue.ini")

    # logger.debug("existedList: " + str(existedList))

    addIpList = list(set(ipList).difference(set(existedList)))

    if len(addIpList) == 0:
        logger.debug("Not changes, thanks.")
        return addIpList

    addIpListToCisco(addIpList)

    for ip in addIpList:
        # print("ip: ", ip)
        config.set("default", ip)

    with open('novalue.ini', 'w') as fp:
        config.write(fp)
    return addIpList

def job():
    getUpdateIpList(getDomainIpList(getItemList("domains.ini")[0]))


def scheduleJob(job):
    from apscheduler.schedulers.blocking import BlockingScheduler

    # BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', seconds=30)
    # scheduler.add_job(job, 'interval', minutes=10)
    # scheduler.add_job(job, 'cron', second=15)
    # nohup python3 -u main.py > test.log 2>&1 &
    scheduler.start()


def main():
    # scheduleJob(job)
    job()
    # pass


if __name__ == "__main__":
    main()
