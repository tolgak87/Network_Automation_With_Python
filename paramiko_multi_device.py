import paramiko
import time

hosts = ["10.1.1.1","10.1.1.2","10.1.1.3"]
command_list = ["show version", "show clock", "show ip route"]

for ip in hosts:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect (ip,22,"admin","cisco")
    commands = client.invoke_shell()

    for command in command_list:
        commands.send(f"{command} \n")
        time.sleep(2)
        output = commands.recv(1000000)
        output = output.decode("utf-8")
        print(output)
