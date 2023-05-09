import telnetlib

host = "10.1.1.1"
user = "admin"
password = "test"

tel = telnetlib.Telnet(host, 23, timeout=2)

tel.read_until(b"Username:")
tel.write(user.encode('ascii') + b"\n")
tel.read_until(b"Password:")
tel.write(password.encode('ascii') + b"\n")

tel.write(b"show version\n")

tel.write(b"exit\n")
print(tel.read_all().decode('ascii'))
