from netmiko.paloalto import PaloAltoPanosSSH

connectConfig = {
    'device_type': 'paloalto_panos',
    'host': '172.16.8.81',
    'username': 'python-api',
    'password': 'python'
}

net_connect = PaloAltoPanosSSH(**connectConfig)

# output = net_connect.send_command('show clock')

# output = net_connect.send_command('set address pythontest001 ip-netmask 255.255.255.0')
# print(output)

config_commands = ['set address test-003 tag insideIP ip-netmask 255.255.255.0',
                   'set address test-004 tag insideIP ip-netmask 255.255.255.0',
                   'set address test-005 tag insideIP ip-netmask 255.255.255.0']
                   # ,"commit"]
# config_commands = ['delete address test-002 tag insideIP']

output = net_connect.send_config_set(config_commands)
print(output)