import telnetlib
import socket

# Define the router's IP address, username, and password
ip_address = "192.168.64.128"
username = "Cisco3"
password = "class1"


# Connect to the router via Telnet
tn = telnetlib.Telnet(ip_address, timeout=0.1)

# Login to the router
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

# Enable privileged mode
tn.write(b"enable\n")
tn.write(b'class1\n')

# Run the 'show users' command
tn.write(b"show users\n")

while True:
    try:
        output = tn.read_some().decode('ascii')
        if output:
            print(output, end='')
    except socket.timeout:
        print("...Exiting the router.")
        break


# Disconnect from the router
#tn.write(b"exit\n")

# Close the Telnet connection
#tn.close()

if tn.close() is None:
    print("Telnet connection closed successfully")
else:
    print("Error closing Telnet connection")