

domainList = ["sbig-gi-sandbox.in.ebaocloud.com", "sbig-gi.in.ebaocloud.com"]

def getDomainIpList(domainList):
    import socket
    retList = []
    for domain in domainList:
        ip = socket.gethostbyname(domain)
        retList.append(ip)
    return retList

# print(getDomainIpList(domainList))

def getUpdateIpList(ipList):
    import configparser
    config = configparser.ConfigParser(allow_no_value=True)

    config.read("novalue.ini")

    keys = config["default"].keys()
    existedList = list(keys)

    print(existedList)

    subtraction = list(set(ipList).difference(set(existedList)))
    print(subtraction)

    for ip in subtraction:
        print("ip: ", ip)
        config.set("default", ip)

    with open('novalue.ini', 'w') as fp:
        config.write(fp)
    return subtraction

def addIpListToCisco(ipList):
    import paramiko  # 导入paramiko模块
    import time  # 导入time模块，这个后面会用到
    host = '172.16.30.250'  # 定义主机IP
    user = 'weifei.shen'  # 定义登录的用户名
    passwd = 'PL24680qw'  # 定义使用的密码
    s = paramiko.SSHClient()  # 实例化，啥意思?请看注释①
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 请看注释②
    s.connect(host, username=user, password=passwd, look_for_keys=False, allow_agent=False)  # 定义登录的IP、用户名和密码
    print('login success.')  # 登录成功提示
    cmd = s.invoke_shell()  # 创建一个交互式的shell，实现多发送条命令
    # cmd.send("conf t \n")   # 发送命令
    # time.sleep(1)           # 睡眠1s，特别重要，注释③
    # cmd.send("int f0/1 \n")
    # time.sleep(1)
    # cmd.send("ip add 1.1.1.2 255.255.255.0 \n")
    # time.sleep(1)
    # cmd.send("end \n")
    # time.sleep(1)
    # cmd.send("show ip int bri\n ")
    cmd.send("show clock\n")
    time.sleep(1)
    cmd.send("show ip int bri\n ")
    time.sleep(1)
    output = cmd.recv(65535)  # 接收输出
    print(output.decode('utf-8', 'ignore'))  # 打印输出
    cmd.close()  # 关闭交互式shell

def main():
    print(getUpdateIpList(getDomainIpList(domainList)))


if __name__ == "__main__":
    main()



 