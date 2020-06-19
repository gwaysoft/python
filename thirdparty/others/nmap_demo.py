import nmap

nm = nmap.PortScanner()
#result = nm.scan(hosts="172.16.7.0/24", arguments="-v -n -sn")
# scan port 22
result = nm.scan(hosts="172.16.7.0/24", arguments="-v -sS -P " + "22, 80")
print(result)

for host in nm.all_hosts():
    print("host: %s (%s)" % (host, nm[host].hostname()))
    print("state: %s" % nm[host].state())