import paramiko


ssh_client = paramiko.SSHClient()

# fix: paramiko.ssh_exception.SSHException: Server '172.16.7.40' not found in known_hosts
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
keyFile = "d:/tmp/id_rsa"
key = paramiko.RSAKey.from_private_key_file(keyFile)
#print(key)
ssh_client.connect(hostname="192.168.2.100", username="root", pkey=key, timeout=5)

stdin, stdout, stderr = ssh_client.exec_command('cd /home; ls')
print(stdout.read())
print("-------------\n")

stdin, stdout, stderr = ssh_client.exec_command('ansible all -a "ls"')
print(stdout.read())
print("-------------\n")
