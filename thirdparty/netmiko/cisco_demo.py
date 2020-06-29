from netmiko import ConnectHandler

connectConfig = {
    'device_type': 'cisco_ios',
    'host': '172.16.30.250',
    'username': 'weifei.shen',
    'password': 'pl24680QW'
}

net_connect = ConnectHandler(**connectConfig)

output = net_connect.send_command('show ip int brief')
print(output)

net_connect = ConnectHandler(**connectConfig)

config_commands = ['ip access-list extended VM',
                   'permit ip any host 13.127.206.51']
output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command("wr")
print(output)

# time.sleep(10)
output = net_connect.send_command("sh running-config | inc any host 13.127.206.51")
print(output)

output = net_connect.send_command("sh startup-config | inc any host 13.127.206.51")
print(output)
