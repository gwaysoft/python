import myLogger
import logging
logger = myLogger.getLogger(fileLevel = logging.DEBUG, fileName="abc.log")

# default parameter
# logger = myLogger.getLogger()

logger.debug("dd")
logger.info("ddddd")
logger.warn("输出")