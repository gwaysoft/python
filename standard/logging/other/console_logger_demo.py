import logging

'''
Level等级 数值  
CRITICAL   50
ERROR      40
WARNING    30
INFO       20
DEBUG      10
NOTSET      0

NOTSET<DEBUG<INFO<WARNING<ERROR<CRITICAL 可以这么理解，包含的关系，一层一层的概括进去
'''
logger = logging.getLogger()
logger.setLevel(logging.INFO) #设置输出等级
ph = logging.StreamHandler()  #创建输出控制台的容器
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s") #配置输出的内容
ph.setFormatter(formatter)   #将配置内容添加到创建的容器里
logger.addHandler(ph)   #将我们的容器添加到handler
logger.info("控制台输出内容")

logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")