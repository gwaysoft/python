from netmiko.paloalto import PaloAltoPanosSSH
import virtualenvwrapper.hook_loader

connectConfig = {
    'device_type': 'paloalto_panos',
    'host': '172.16.8.81',
    'username': 'python-api',
    'password': 'python'
}

net_connect = PaloAltoPanosSSH(**connectConfig)

# output = net_connect.send_command('show clock')
output = net_connect.send_command('show object dynamic-address-group name awsprodw')
# output = net_connect.send_command('show object dynamic-address-group name cloud-env')
print(type(output))
outList = output.split("\n")
tempList = ["Dynamic address groups in vsys vsys1:",
            "----------------------------------------------------",
            "",
            "----------------defined in vsys --------------------",
            "----------------defined in shared-------------------",
            "O: address object; R: registered ip; D: dynamic group; S: static group"]

print(outList[:10:])

print("-----------start--------------")
tagList = []
for item in outList[8:len(outList) - 4:]:
    tagList.append(item.strip().replace(" (O)", ""))
print("-----------end--------------")
print(len(tagList))

# config_commands = ['set address test-003 tag cloud-env ip-netmask 255.255.255.0',
#                    "commit"]
# config_commands = ['delete address test-002 tag insideIP']

# output = net_connect.send_config_set(config_commands)
# print(output)
