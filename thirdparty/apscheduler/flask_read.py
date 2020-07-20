from apscheduler.jobstores.mongodb import MongoDBJobStore
from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    # 配置执行job
    JOBS = [
        {
            'id': 'job1',
            'func': 'flask_read:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        }
    ]
    # 存储位置
    SCHEDULER_JOBSTORES = {
        'mongo': MongoDBJobStore(host='192.168.2.110', database='test', username="root", password="root")
    }
    # 线程池配置
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    # 调度器开关
    SCHEDULER_API_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b))


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler = APScheduler()
    # 注册app
    scheduler.init_app(app)
    scheduler.start()

    app.run(host="192.168.2.110")
