from netmiko.paloalto import PaloAltoPanosSSH

connectConfig = {
    'device_type': 'paloalto_panos',
    'host': '172.16.8.81',
    'username': 'python-api',
    'password': 'python'
}


def executeCommand(command):
    net_connect = PaloAltoPanosSSH(**connectConfig)
    return net_connect.send_command(command)


def executeConfigCommand(config_commands):
    print(config_commands)
    if len(config_commands) == 0:
        return
    config_commands.append("commit")
    net_connect = PaloAltoPanosSSH(**connectConfig)
    return net_connect.send_config_set(config_commands)



