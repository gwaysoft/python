import paramiko

transport = paramiko.Transport(("192.168.2.100", 22))
transport.connect(username="root", password="root")

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get("/root/id_rsa", "d:/id_rsa")
sftp.close()