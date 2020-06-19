oa#w!/usr/bin/evn python
#-*-coding:utf-8 -*-

# yum install graphviz            // 为了使用dot命令
# yum install ImageMagick         // 为了使用/usr/bin/convert命令
 
import os,sys,time,subprocess
import warnings,logging
from scapy.all import traceroute
from scapy.as_resolvers import AS_resolver_radb
 
warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtine").setLevel(logging.ERROR)
 
domains = input('please input the domain or IP what you want: ') # oa.ebaotech.com
target = domains.split(" ")
dport = [80, 21]
 
if len(target) >= 1 and target[0] != '':
    # 启动路由跟踪
    res, unans = traceroute(target, dport=dport, retry=-2)
    # traceroute 生成的信息绘制成svg
    # res.graph(target="> graph.svg")
    res.graph(target="> graph.svg", ASres=AS_resolver_radb(), type="svg")
    time.sleep(2)
    # svg 转格式为 png
    subprocess.Popen("/usr/bin/convert graph.svg graph.png", shell=True)
else:
    print("IP/domain number of errors, exit")   