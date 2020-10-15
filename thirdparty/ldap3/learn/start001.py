from ldap3 import Server, Connection, SAFE_SYNC
my_server = "ldap://ebaotech.com:389"
my_user = "MISAD"
my_password = "dt_P6NbY"

server = Server(my_server)
conn = Connection(server, my_user, my_password, strategy=SAFE_SYNC, auto_bind=True)
status, result, response, _ = conn.search('o=test', '(objectclass=*)')  # usually you don't need the original request (4th element of the return tuple)