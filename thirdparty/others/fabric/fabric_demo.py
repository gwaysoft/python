from fabric.api import run
from fabric.api import env

env.hosts = ["localhost", "192.168.2.129"]

env.user = "root"
env.password = "root"
env.port = "22"

def hostname():
    run("hostname")

def ls(path="."):
    run("ls {}".format(path))

def tail(path "/etc/passwd", line 10):
    run("tail -n {0} {1}".format(line.path))