from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
# scheduler.add_job(job, 'interval', seconds=10)


scheduler.add_job(job, 'cron', second =10)
scheduler.start()