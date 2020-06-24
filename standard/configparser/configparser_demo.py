import configparser

config = configparser.ConfigParser(allow_no_value=True)

config["DEFAULT"].keys = ["d","333"]

with open("demain.ini","w") as configfile:
    config.write(configfile)