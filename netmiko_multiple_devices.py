from netmiko import Netmiko

host1 = {
    "host": "10.1.1.1",
    "username": "admin",
    "password": "test",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1
}

host2 = {
    "host": "10.1.1.2",
    "username": "admin",
    "password": "test",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1
}

host3 = {
    "host": "10.1.1.3",
    "username": "admin",
    "password": "test",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1
}

devices = [host1, host2, host3]

for host in devices:
    net_connect = Netmiko(**host)
    config = ["interface gigabitethernet 1/2", "description new_port"]
    command = "show version"
    config_output = net_connect.send_config_set(config)
    show_output = net_connect.send_command(command)
    net_connect.disconnect()
    print(config_output)
    print(show_output)
