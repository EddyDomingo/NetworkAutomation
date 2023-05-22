import getpass
import telnetlib

user1 = input ('enter your telnet username: ')
password1 = getpass.getpass()

IP1 = '192.168.31.223' # IP = '10.2.162.206'

print('Connection to Router ' + (IP1))
HOST1 = IP1

tn = telnetlib.Telnet(HOST1, 23)
tn.read_until(b'Username: ') #read_until
tn.write(user1.encode('ascii') + b'\n')

if password1:
    tn.read_until(b'Password: ') #read_until
    tn.write(password1.encode('ascii') + b'\n')
tn.write(b'enable\n')
tn.write(b'class1\n')
tn.write(b'show users\n')
tn.write(b'show ip route\n')
print(tn.read_all().decode('ascii'))

# Disconnect from the router
tn.write(b"exit\n")

tn.read_until()
