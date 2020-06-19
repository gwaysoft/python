
def getFileLogger(level):
    import logging
    from logging.handlers import TimedRotatingFileHandler

    # formatter
    fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] %(name)s - %(levelname)s: %(message)s"
    dateFmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=fmt, datefmt=dateFmt)

    # log directory
    import os
    genpath = os.getcwd()
    logpath = os.path.join(genpath,"log") #拼接log文件路径

    if os.path.exists(logpath): #判断路径是否存在，不存在则创建
        pass
    else:
        os.makedirs(logpath)
    logFileName = logpath+"/log.log"

    # handler
    # when="D" day "W0" sunday
    # backupCount = 30 30天 保留时间
    handler = TimedRotatingFileHandler(logFileName, when="D",backupCount=30)
    handler.setFormatter(formatter)


    # logger
    logger = logging.getLogger("time")
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
import logging
logf = getFileLogger(logging.DEBUG)

logf.info("info")
logf.debug("debug")
logf.warning("warning")
logf.error("error")
logf.critical("critical")