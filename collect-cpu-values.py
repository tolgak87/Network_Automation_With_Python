import paramiko
import time
import re
from pandas import DataFrame

c = open("Command_List.txt", "r")
command_list = c.read().split("\n")                                #Create a List from Command_List file

d = open("Device_List.txt", "r")
hosts = d.read().split("\n")                                       #Create a List from Device_List file

port = 22
username = "root"
password = "Test1234."
logs = []
logs1= []
lista = []
listb = []
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
    device_name = re.findall("<\w+\W+\w+>", logs1)                     #Find device name between < >
    cpu_level = re.findall("CPU Usage            : \d+%", logs1)       #Find CPU Usage value line
    device = device_name[0]
    device = ''.join(map(str, device))
    device = re.sub("<","",device)                                     #Remove "<" from Device name
    device = re.sub(">","",device)                                     #Remove ">" from Device name
    cpu = ''.join(map(str, cpu_level))
    cpu = re.findall("[0-9]+%",cpu)                                    #Find CPU value
    cpu = ''.join(map(str, cpu))
    lista.append(device)                                               #Add each device name to lista
    listb.append(cpu)                                                  #Add each cpu value to lista
    with open("{}.txt".format(ip), "w") as f:                          #Open txt file named by hosts(ip) in for loop
        f.write(logs1)                                                 #Write string to file
    logs1 = []                                                         #Empty list after each for loop

print("lista=",lista)
print("listb",listb)
df = DataFrame({'NE Name': lista, 'CPU Value': listb })                #Create data frame with device name and cpu level

df.to_excel('CPU Levels.xlsx', sheet_name='CPU LEVELS', index=False)   #Create excel file and insert dataframe into excel file
