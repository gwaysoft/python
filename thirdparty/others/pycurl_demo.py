# -*- coding: UTF-8 -*-

import os
import sys
import pycurl

#URL = "http://pycurl.io/docs/latest/index.html"
URL = "http://www.baidu.com"

c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.TIMEOUT, 50)
c.setopt(pycurl.CONNECTTIMEOUT, 50)
c.setopt(pycurl.FORBID_REUSE, 1)
c.setopt(pycurl.NOPROGRESS, 1)

try:
    c.perform()
except Exception as e:
    c.close()
    print(e)
    sys.exit()
print("\ncode: %s" %c.getinfo(c.HTTP_CODE))
print("time: %2f ms" %c.getinfo(c.CONNECT_TIME))
print("time: %2f ms" %c.getinfo(c.SPEED_DOWNLOAD))