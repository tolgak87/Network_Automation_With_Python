import subprocess
reached = []                                                #Empty list to collect reachable hosts
not_reached = []                                            #Empty list to collect unreachable hosts
hosts = ["192.168.1.1","123.214.2.2","www.google.com",]     #Hosts list
for ip in hosts:
    ping_test = subprocess.call('ping %s -n 2' % ip)        #Ping host n times
    if ping_test == 0:                                      #If ping test is 0, it' reachable
        reached.append(ip)
    else:
        not_reached.append(ip)                              #Else, it's not reachable
print("{} is reachable".format(reached))
print("{} not reachable".format(not_reached))
