def getSynAddrList():
    import requests
    import re
    text = requests.get(
        "http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
    # itemLength = 63
    list01 = text.split("\n")
    returnList = []
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    tag = " tag cloud-env"
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                text = "set address "
                if item == "null":
                    continue

                if re.match(pattern, item):
                    # continue
                    text = text + item[:63:] + tag + " ip-netmask " + item
                else:
                    # if len(item) >= 63:
                    text = text + item[:63:] + tag + " fqdn " + item
                returnList.append(text)
    return returnList


def delSynAddrList():
    import requests
    text = requests.get(
        "http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
    # itemLength = 63
    list01 = text.split("\n")
    returnList = []
    tag = " tag insideIP"
    for line in list01:
        if line.find(",") != -1:
            lineList = line.split(",")
            for item in lineList:
                text = 'delete address '
                if item == "null":
                    continue
                text = text + item[:63:] + tag
                returnList.append(text)
    return returnList


def addAddress(addrList):
    # config_commands = list(addrList[0:2])
    config_commands = list(addrList)
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

    # output = net_connect.send_command('show clock')

    # output = net_connect.send_command('set address pythontest001 ip-netmask 255.255.255.0')
    # print(output)

    # config_commands = ['set address test-003 tag insideIP ip-netmask 255.255.255.0',
    #                    'set address test-004 tag insideIP ip-netmask 255.255.255.0',
    #                    'set address test-006 tag insideIP ip-netmask 255.255.255.0',
    #                    "commit"]
    # config_commands = ['delete address test-002 tag insideIP']


def main():
    addAddress(getSynAddrList())
    # addAddress(delSynAddrList())


if __name__ == "__main__":
    main()
