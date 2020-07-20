import paramiko

transport = paramiko.Transport(("192.168.2.110", 22))
transport.connect(username="root", password="root")

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get("/root/test.log", "d:/tmp/test.log")
sftp.close()