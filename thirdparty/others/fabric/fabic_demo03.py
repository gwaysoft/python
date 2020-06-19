from fabric.api import *

env.user = "root"
env.password = "root"
env.port = 22
env.warn_only = True

env.hosts=["192.168.2.100", "192.168.2.101"]

env.roledefs = {
    "web":["192.168.2.100"],
    "db": ["192.168.2.101"]
}

def install_redis():
    run("yum install -y redis", shell=False)

def reboot_redis():
    run("systemctl start redis", shell=False)

@task
@roles("db")
def deploy_db():
    install_redis()
    reboot_redis()
    print("db installed")


@task
@roles("web")
def run_web():
    put("/root/myapp.py", "/root/python/myapp.py")
    with cd("~/python"):
         run("gunicorn -b 0.0.0.0:8000 myapp:app -D", pty=False)
         print("web installed")

@task
@roles("web")
def stop_web():
    with cd()

# netstat -hpl | grep 8000
# rpm -aq | grep redis
