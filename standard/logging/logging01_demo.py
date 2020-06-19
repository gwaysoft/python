import logging
from logging.handlers import TimedRotatingFileHandler

# formatter
fmt = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
dateFmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt=fmt, datefmt=dateFmt)

# handler
# when="D" day "W0" sunday
# backupCount = 30 30天 保留时间
handler = TimedRotatingFileHandler("./standard/logging/time.log", when="D",backupCount=30)
handler.setFormatter(formatter)


# logger
logger = logging.getLogger("time")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")