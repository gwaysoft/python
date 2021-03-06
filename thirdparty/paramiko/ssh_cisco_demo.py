#!/usr/bin/env python
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

# cmd.send("conf t\n")  # 发送命令
# time.sleep(1)  # 睡眠1s，特别重要，注释③
#
# cmd.send("ip access-list extended VM\n")
# time.sleep(1)
#
# cmd.send("permit ip any host 13.127.206.46\n")
# time.sleep(1)
#
# cmd.send("end\n")
# time.sleep(1)
#
# cmd.send("wr\n")
# time.sleep(1)



# cmd.send("sh startup-config | inc any \n")
# cmd.send("sh startup-config | inc any host 172.16.30.20 \n")

# cmd.send("sh startup-config | inc any host 13.127.206.46\n")
# time.sleep(3)

cmd.send("iox \n")
time.sleep(3)

output = cmd.recv(65535)  # 接收输出
print("OUT: ", output.decode('utf-8', 'ignore'))  # 打印输出
cmd.close()  # 关闭交互式shell


# cmd.send("int f0/1 \n")
# time.sleep(1)
# cmd.send("ip add 1.1.1.2 255.255.255.0 \n")
# time.sleep(1)
# cmd.send("end \n")
# time.sleep(1)
# cmd.send("show ip int bri\n ")
# cmd.send("show clock\n")
# time.sleep(1)
# cmd.send("show ip int bri\n ")
# time.sleep(1)
# cmd.send("wr \n")
# time.sleep(1)
