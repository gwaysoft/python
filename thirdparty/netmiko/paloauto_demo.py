from netmiko.paloalto import PaloAltoPanosSSH
import virtualenvwrapper.hook_loader

connectConfig = {
    'device_type': 'paloalto_panos',
    'host': '172.16.8.81',
    'username': 'python-api',
    'password': 'python'
}

net_connect = PaloAltoPanosSSH(**connectConfig)

output = net_connect.send_command('show clock')
print(output)



config_commands = ['set address test-003 tag cloud-env ip-netmask 255.255.255.0',
                   "commit"]
# config_commands = ['delete address test-002 tag insideIP']

output = net_connect.send_config_set(config_commands)
print(output)
