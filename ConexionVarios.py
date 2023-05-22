from getpass import getpass
import telnetlib

user = input ('enter your telnet username: ')
password = getpass.getpass()

f = open('file.txt')

for IP in f:
    IP = IP.strip()
    print ('configuring router ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b'conf t\n')
    for n in range (2,101):
        tn.write(b'vlan ' + str(n).encode('ascii') + b'/n')
        tn.write(b'name Python_VLAN ' + str(n).encode('ascii') + b'/n')
        print('Creando VLAN' + str)