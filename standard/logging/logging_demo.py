import logging


# formatter
fmt = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
dateFmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt=fmt, datefmt=dateFmt)


# str = "d"
str = __name__
# filter
filter1 = logging.Filter(str)



# file
fileHandler = logging.FileHandler("./standard/logging/log.txt")
fileHandler.setFormatter(formatter)
fileHandler.addFilter(filter1)

# handler
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)


# logger
logger = logging.getLogger(str)
logger.setLevel(level = logging.DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)





logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")