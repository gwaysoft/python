import paramiko

'''
ssh_client = paramiko.SSHClient()

# fix: paramiko.ssh_exception.SSHException: Server '172.16.7.40' not found in known_hosts
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname="172.16.7.40", port=22, username="oa_uat_tomcat", password="oa_uat_tomcat")

stdin, stdout, stderr = ssh_client.exec_command("df")
print(stdout.read())

ssh_client.close()
'''

transport = paramiko.Transport(("172.16.7.40", 22))
transport.connect(username="oa_uat_tomcat", password="oa_uat_tomcat")

sftp = paramiko.SFTPClient.from_transport(transport)
#sftp.get("/home/oa_uat_tomcat/temp.txt","d:/tmp/temp.txt")
sftp.put("d:/tmp/temp1.txt","/home/oa_uat_tomcat/temp.txt")
sftp.close()
