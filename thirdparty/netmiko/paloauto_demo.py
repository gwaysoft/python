from netmiko.paloalto import PaloAltoPanosSSH

connectConfig = {
    'device_type': 'paloalto_panos',
    'host': '172.16.8.81',
    'username': 'python',
    'password': 'python'
}

net_connect = PaloAltoPanosSSH(**connectConfig)

output = net_connect.send_command('show clock')
print(output)
