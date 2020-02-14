import subprocess
reached = []
not_reached = []
hosts = ["192.168.1.1","123.214.2.2","www.google.com",]
for ip in hosts:
    ping_test = subprocess.call('ping %s -n 2' % ip)
    if ping_test == 0:
        reached.append(ip)
    else:
        not_reached.append(ip)
print("{} is reachable".format(reached))
print("{} not reachable".format(not_reached))