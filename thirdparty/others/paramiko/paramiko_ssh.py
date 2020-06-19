import paramiko

ssh_client = paramiko.SSHClient()

# fix: paramiko.ssh_exception.SSHException: Server '172.16.7.40' not found in known_hosts
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname="172.16.7.40", username="oa_uat_tomcat", password="oa_uat_tomcat", timeout=5)

stdin, stdout, stderr = ssh_client.exec_command('cd /home/<user>/; ls -al')
print(stdout.read())
print("-------------\n")

#stdin, stdout, stderr = ssh_client.exec_command("cd /home/<user>;ll -a")

#print(stdout.read())
ssh_client.close()