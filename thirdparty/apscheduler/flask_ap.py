#
# test script
# curl -i -X POST -H "'Content-type':'appon/x-www-form-urlencoded', 'charset':'utf-8', 'Accept': 'text/plain'" -d '{"id":"job5","func": "test:job1","args":"(\"aaa\",\"aaadd\")","trigger":"interval","seconds":60}' http://127.0.0.1:5000/addjob
#
# curl -i -X POST -H "'Content-type':'appon/x-www-form-urlencoded', 'charset':'utf-8', 'Accept': 'text/plain'" -d '{"id":"job5","func":"job3","args":"(\"aaaaadd\")","trigger":"interval","seconds":60}' http://192.168.2.110:5000/addjob
# pip install flask
# pip install Flask-APScheduler
from flask import Flask
from flask_apscheduler import APScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from flask import request
import os
import time

app = Flask(__name__)
scheduler = APScheduler()


class Config(object):
    JOBS = []
    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(host='192.168.2.110', database='apschedulesr',collection='job',  username="root", password="root")
    }
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_API_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b) + '   ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def job2(a):
    py = 'python wx_post_test.py ' + a
    os.system(py)

def job3():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def jobfromparm(**jobargs):
    id = jobargs['id']
    func = jobargs['func']
    args = eval(jobargs['args'])
    print(args)
    trigger = jobargs['trigger']
    seconds = jobargs['seconds']
    print('add job: ', id)
    job = scheduler.add_job(func="flask_ap:job3", id="100",  trigger="interval", seconds=5, replace_existing=True)
    return job

@app.route('/test')
def test():
    print("test")
    return "Success!"


@app.route('/pause/<name>')
def pausejob(name):
    scheduler.pause_job(name)
    return "Success!"


@app.route('/resume/<name>')
def resumejob(name):
    scheduler.resume_job(name)
    return "Success!"


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    print("add")
    data = request.get_json(force=True)
    print(data)
    job = jobfromparm(**data)
    return 'sucess'


if __name__ == '__main__':
    # app = Flask(__name__)
    app.config.from_object(Config())
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug = True, host="192.168.2.110")
