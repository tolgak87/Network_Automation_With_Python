import paramiko
import time

c = open("Command_List.txt", "r")
command_list = c.read().split("\n")                                #Create a List from Command_List file

d = open("Device_List.txt", "r")
hosts = d.read().split("\n")                                       #Create a List from Device_List file

port = 22
username = "root"
password = "Test1234."
logs = []
logs1= []

for ip in hosts:                                                   #Loop each ip in hosts list
    print("Try to login:", ip)
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(ip, port, username, password)
    comm = conn.invoke_shell()
    comm.send("s 0 t \n")
    for command in command_list:                                    #Loop each commmand in command_list
        comm.send(' %s \n' %command)
        time.sleep(.5)
        output = comm.recv(65535)
        output = output.decode("utf-8")
        logs = output.split("xxxxx")   #Convert string to List without any change
        print("logs",logs)
        logs1.extend(logs)                                             #Extend list with new logs list in for loop
    logs1 = ''.join(map(str, logs1))                                   #Convert list to string
    with open("{}.txt".format(ip), "w") as f:                          #Open txt file named by hosts(ip) in for loop
        f.write(logs1)                                                 #Write string to file
    logs1 = []                                                         #Empty list after each for loop
