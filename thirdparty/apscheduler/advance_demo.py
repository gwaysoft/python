from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from pymongo import MongoClient

# client = MongoClient('192.168.2.110',
#                      username='admin',
#                      password='123456',
#                      authSource='admin',
#                      authMechanism='SCRAM-SHA-256')

# client = MongoClient('192.168.2.110',
#                      username='admin',
#                      password='123456')
#
# print(client.list_databases())


def alarm(time):
    print('Alarm!dd This alarm was scheduled at %s.' % time)


jobstores = {
    'mongo': MongoDBJobStore(host='192.168.2.110', database='apschedulesr',username="root", password="root")
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(10)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
# scheduler.add_job(alarm, args=[datetime], id='job_interval', trigger='interval', seconds=5,
#                   replace_existing=True)
try:
    scheduler.start()
except SystemExit:
    print('exit')
    exit()
