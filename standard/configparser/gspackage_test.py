from gspackage import comparison as cp, config

print(cp.getAddItems(items={"3","2","33"}))
print(cp.getDelItems(items={"3","2","33"}))



# print(gsconfigparser.getAbsFile("d"))

def job():
    print(config.getValue(key="def"))
    print(config.getValue(key="def01"))

    print(config.getValue(section="log", key="log1"))
    print(config.getValue(section="log", key="log2"))

def scheduleJob(job):
    from apscheduler.schedulers.blocking import BlockingScheduler

    # BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', seconds=10)
    # scheduler.add_job(job, 'interval', hours=6)
    # scheduler.add_job(job, 'interval', minutes=2)
    # scheduler.add_job(job, 'cron', second=15)
    # nohup python3 -u business01.py > test.log 2>&1 &
    scheduler.start()
# scheduleJob(job)