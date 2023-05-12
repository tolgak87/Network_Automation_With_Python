from netmiko import Netmiko
import re

host = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]

check_ip = "192.162.10.4"
duplicated_list = []

for ip in host:
    device = {"host": ip,
               "username": "admin",
               "password": "test",
               "device_type": "cisco_ios",
               "global_delay_factor": 0.1
               }

    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip interface brief")
    duplicate_ip = re.findall(check_ip, output)

    while duplicate_ip:
        interface = re.findall(f"(.*){check_ip}", output)
        duplicated_list.append(check_ip)
        duplicated_device_ip = ip
        break

if duplicated_list:
    print(f"---------\nDuplicated IP: {check_ip} \nDuplicated Device IP Address: {duplicated_device_ip} \nInterface: {interface[0]} \n -----------")
else:
    print(f"{check_ip} IP address is suitable for use")
