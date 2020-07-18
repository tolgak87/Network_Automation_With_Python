import json
from netmiko import Netmiko

c = open("Command_Set.txt", "r")                                    # Get Command list from file
command_set = c.read().split("\n")                                  # Convert each command into a list

d = open("Command_List.txt", "r")
command_list = d.read().split("\n")                                 #Create a List from Device_List file

with open('host.json') as file:                                     #Open json file
  logs = json.load(file)                                            #Load json file to "data" dictionary
logs1 = []

for device in logs:
    net_connect = Netmiko(**logs[device])
    print("Connected to:", net_connect.find_prompt())               # Display hostname
    output = net_connect.send_config_set(command_set)               # Run config sets(configuration commands)
    output += net_connect.send_command("display device")            # Run 1 Display command
    output += net_connect.send_config_set(command_list)             # Run Multiple display commands
    with open("{}.txt".format(device), "w") as f:                   # Open txt file named by hosts(ip) in for loop
        f.write(output)                                             # Write string to file
    logs1 = []
    net_connect.disconnect()                                        # Disconnect from Session
    print(output)
