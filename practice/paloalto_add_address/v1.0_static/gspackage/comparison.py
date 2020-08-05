def getAbsFile(fileName="comparison.ini"):
    import os
    return os.path.abspath(os.path.dirname(__file__)) + "/" + fileName


def getConfig(fileName="comparison.ini"):
    import configparser
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(getAbsFile(fileName))
    return config


def getItems(fileName="comparison.ini"):
    config = getConfig(fileName)
    keys = config["DEFAULT"].keys()
    return set(keys)


def addItems(fileName="comparison.ini", items={}):
    config = getConfig(fileName)
    for item in items:
        config.set("DEFAULT", item)

    with open(getAbsFile(fileName), "w") as configfile:
        config.write(configfile)


def delItems(fileName="comparison.ini", items={}):
    config = getConfig(fileName)
    for item in items:
        config.remove_option("DEFAULT", item)
    with open(getAbsFile(fileName), "w") as configfile:
        config.write(configfile)


def getAddItems(fileName="comparison.ini", items={}):
    return items - getItems(fileName)


def getDelItems(fileName="comparison.ini", items={}):
    return getItems(fileName) - items


def resetItemList(fileName="comparison.ini", items={}):
    addItems(fileName, getAddItems(fileName, items))
    delItems(fileName, getDelItems(fileName, items))
