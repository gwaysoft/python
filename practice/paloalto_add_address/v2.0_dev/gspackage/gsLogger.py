import logging

def getMyLogger(consoleLevel=logging.DEBUG, fileLevel=logging.INFO, logDir="temp", fileName="log.log"):
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    # log directory
    # import os
    # genpath = os.getcwd()
    # logpath = os.path.join(genpath, "log")  # 拼接log文件路径
    #
    # if os.path.exists(logpath):  # 判断路径是否存在，不存在则创建
    #     pass
    # else:
    #     os.makedirs(logpath)
    # logFileName = logpath + "/log.log"

    import os
    logpath = "/var/log/python/" + logDir  # 拼接log文件路径

    if os.path.exists(logpath):  # 判断路径是否存在，不存在则创建
        pass
    else:
        os.makedirs(logpath)
    logFileName = logpath + "/" + fileName
    from logging.handlers import TimedRotatingFileHandler
    fh = TimedRotatingFileHandler(logFileName, when="D", backupCount=30)
    fh.setLevel(fileLevel)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(consoleLevel)
    # create formatter and add it to the handlers
    currentFormat = logging.Formatter(
        '%(asctime)s - pid [%(process)d] - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')
    ch.setFormatter(currentFormat)
    fh.setFormatter(currentFormat)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

