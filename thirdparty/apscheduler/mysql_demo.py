from datetime import datetime, timedelta
import sys
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def alarm(time):
    print('Alarm!dd This alarm was scheduled at %s.' % time)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    url="mysql+pymysql://root:123456@192.168.2.110/test?charset=utf8"
    scheduler.add_jobstore('sqlalchemy', url=url,tablename='api_job')
    # alarm_time = datetime.now() + timedelta(seconds=10)
    # # scheduler.add_job(alarm, 'date', run_date=alarm_time, args=[datetime.now()])
    # scheduler.add_job(alarm, args=[datetime.now(), ], id='job_interval', trigger='interval', seconds=5,
    #                  replace_existing=True)
    print('To clear the alarms, delete the example.sqlite file.')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass