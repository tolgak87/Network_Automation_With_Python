from netmiko import Netmiko

device = {
"host": "10.1.1.1",
"username": "admin",
"password": "test",
"device_type": "cisco_ios",
"global_delay_factor": 0.1,
}

net_connect = Netmiko(**device)

config= ["interface GigabitEthernet1/2", "description new_port"]
command = "show run interface GigabitEthernet1/2"

config_output = net_connect.send_config_set(config)

show_output = net_connect.send_command(command)
net_connect.disconnect()

print(config_output)
print(show_output)
