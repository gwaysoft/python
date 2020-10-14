from gspackage.logging.gsLogger import getMyLogger
from gspackage.utils import config

logger = getMyLogger(logDir=config.getValue(section="LOG", key="log_dir"), fileName="address.log")
