import sys
import os
from datetime import datetime
import hpilo
import multiprocessing
import time

def log(log):
    today = datetime.now()
    date = today.strftime("%y-%m-%d")
    path = os.getcwd()
    file = open(os.path.join(path,"oli_" + date)+".log","a+")
    file.write(today.isoformat() + " | " + log +"\n")
    file.close()

def job(ip):
    #time.sleep(interval)
    username = "admin"
    password = "Gq34Ko90"
    print(ip, username, "password")
    ilo = hpilo.Ilo(ip, username, password) 
    b = False
    try:
        print(ip, "start cold boot")
        #ilo.cold_boot_server()
        b = True
        #print(b)
        pass
    except Exception as identifier:
        if(identifier != 'The read operation timed out'):
            b = True
        #print(b)
        pass
    finally:
        if(b):
            print(ip, " cold boot successful")
        else:
            print(ip, " cold boot failed")
        log(ip + " " + ("cold boot successful" if b else "cold boot failed"))
        pass

if __name__ == "__main__":
    try:
        log("job start")
        ip = sys.argv[1]
        p = multiprocessing.Process(target = job, args = (ip, ))
        p.start()
        pass
    except Exception as identifier:
        print("please input ip username password")
        log("error: please input ip username password")
        pass
    finally:
        pass
print(sep="\n")
# python hpilo_test.py 172.16.32.117 admin Gq34Ko90