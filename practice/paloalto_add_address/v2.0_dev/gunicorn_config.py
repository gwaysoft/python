# config.py
import os

bind = "0.0.0.0:5000"
# pidfile = "log/gunicorn.pid"
# accesslog = "log/access.log"
# errorlog = "log/debug.log"
# daemon = True

cwd = os.path.split(os.path.abspath(__file__))[0]
accesslog = os.path.join(cwd, "log/gunicorn.log")

# loglevel = 'debug'
# logfile = os.path.join(cwd, "debug.log")
# logfile = 'debug.log'

workers = 2
timeout = 100


