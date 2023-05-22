import telnetlib
import time


# Definir archivo con information de routers y leer datos
filename = "routers.txt"
with open(filename) as f:
    routers = [line.strip().split(",") for line in f]

for router in routers:
    tn = telnetlib.Telnet(router[0])

    # Ingresar al dispositivo
    tn.read_until(b"Username: ")
    tn.write(router[1].encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(router[2].encode('ascii') + b"\n")

    # Ingreasar a modo privilegiado 
    tn.write(b"enable\n")
    tn.read_until(b"Password: ")
    tn.write(router[2].encode('ascii') + b"\n")

    # Crear direccion Loopback
    tn.write(b"conf t\n")
    tn.write(b"interface loopback 0\n")
    tn.write(f"ip address {router[3]}\n".encode('ascii'))
    tn.write(b"exit\n")

    # Configurar OSPF
    tn.write(b"conf t\n")
    tn.write(b"router ospf 1\n")
    tn.write(f"network {router[5]} area 0\n".encode('ascii'))
    tn.write(f"network {router[6]} 0.0.0.0 area 0\n".encode('ascii'))
    tn.write(b"end\n")

    # Mostrar comando show ip protocols

    tn.write(b"show ip protocols\n")
    time.sleep(1)
    output = tn.read_very_eager().decode('ascii')
    print(output)
    tn.write(b"exit\n")

    # Solicitar el usuario presionar enter para continuar

    input ( f"El router {router[4]} se configuro exitosamente quiere continuar ?")