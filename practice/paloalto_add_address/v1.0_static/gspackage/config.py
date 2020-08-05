def getAbsFile(filename="config.ini"):
    import os
    currentDir = os.path.abspath(os.path.dirname(__file__))
    fatherDir = os.path.dirname(currentDir)
    return fatherDir + "/" + filename


def getConfig(fileName="config.ini"):
    import configparser
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(getAbsFile(fileName))
    return config


def getValue(fileName="config.ini", section="DEFAULT", key="top"):
    config = getConfig(fileName)
    return config[section][key]
