import paramiko
import sys

bl_client = paramiko.SSHClient()
bl_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
bl_client.connect(hostname="192.168.2.100", username="root", password="root")

stdin, stdout, stderr = bl_client.exec_command('cd /home; ls')
print(stdout.read())
print("-------------\n")

channel = bl_client.invoke_shell()
channel.settimeout(20)

buff = ''
resp = ''



channel.send("ssh root@192.168.2.129\n")

#"root@192.168.2.129's password: "
passInfo = "password: \""

while not buff.endswith(passInfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print(e)
        channel.close()
        bl_client.close()
        sys.exit()
    buff += str(resp)
    print(buff, str(buff).endswith(passInfo))


channel.send("root\n")
print("  ",buff)
#channel.send("ifconfig\n")
buff=""

try:
    while buff.find("#") == -1:
        resp = channel.recv(9999)
        buff += str(resp)
except Exception as e:
    print(e)

print(buff)
print("----------")

channel.send("ifconfig\n")
print("  ",buff)
#channel.send("ifconfig\n")
buff=""

try:
    while buff.find("#") == -1:
        resp = channel.recv(9999)
        buff += str(resp)
except Exception as e:
    print(e)

print(buff)
channel.close()
