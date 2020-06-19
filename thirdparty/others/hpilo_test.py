import sys
import hpilo

try:
    ip = sys.argv[1]
    username = "admin"
    password = "Gq34Ko90"
    #username = sys.argv[2]
    #password = sys.argv[3]
    pass
except Exception as identifier:
    print("please input ip username password")
    exit()
    pass

print(ip, username, "password")
ilo = hpilo.Ilo(ip, username, password) 
b = False
try:
    print(ip, "start cold boot")
    ilo.cold_boot_server()
    b = True
    print(b)
    pass
except Exception as identifier:
    if(identifier == 'The read operation timed out')
        b = True
    print(b)
    pass
finally:
    if(b):
        print(ip, " cold boot successful")
    else:
        print(ip, " cold boot failed")
    pass

# python hpilo_test.py 172.16.32.117 admin Gq34Ko90