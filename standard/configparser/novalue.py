import configparser
config = configparser.ConfigParser(allow_no_value=True)

config.read("novalue.ini")

keys = config["zone2"].keys()
print(keys, type(keys), list(keys))

for i in config["zone2"].keys():
    print(i)


zone4 = "zone4"
config.add_section(zone4)
config.set(zone4, 'comment here')
config.set(zone4, 'test',"wwE")
with open('novalue.ini', 'w') as fp:
    config.write(fp)
