from fabric.api import *

env.user = "root"
#env.password = "root"

env.hosts=["192.168.2.129", "192.168.2.101"]
env.passwords = {
    "root@192.168.2.129":"root",
    "root@192.168.2.101":"root",
}

env.roledefs = {
    "db":["192.168.2.129"],
    "web":["192.168.2.101"]
}

@runs_once
def input_raw():
    return prompt("please input directory: ", default="/root")

def worktask(dirname):
    run("ls -l " + dirname)

@task
def go():
    getdir = input_raw()
    worktask(getdir)

# [root@localhost fabric]# fab -f fabric_demo02.py hello:nbc
@task
@roles("db")
def hello(name = "world"):
    print("hello.db %s" % name)

@task
@roles("web")
def hello2(name = "world"):
    print("hello.web %s" % name)

@task
def exec_all():
    execute(hello)
    execute(hello2)