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

    #Asignar Direccion IP en Segmentos
    tn.write(b"conf t\n")
    tn.write(f"interface {router[5]}\n".encode('ascii'))
    tn.write(f"ip address {router[7]}\n".encode('ascii'))
    tn.write(b"no shutdown\n")
    tn.write(b"exit\n")


    if router[0] == '192.168.234.130':
        tn.write(f"interface {router[8]}\n".encode('ascii'))
        tn.write(f"ip address {router[9]}\n".encode('ascii'))
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")


    # Crear direccion Loopback
    tn.write(b"interface loopback 0\n")
    tn.write(f"ip address {router[3]}\n".encode('ascii'))
    tn.write(b"exit\n")

    #Configuracion OSPF
    tn.write(b"router ospf 1\n")
    tn.write(f"network {router[6]} 0.0.0.0 area 0\n".encode('ascii'))

    # Routers configuracion
    if router[0] == '192.168.234.129':
        tn.write(b"network 10.0.0.0 0.0.0.255 area 0\n")
    elif  router[0] == '192.168.234.130':
        tn.write(b"network 10.0.0.0 0.0.0.255 area 0\n")
        tn.write(b"network 20.0.0.0 0.0.0.255 area 0\n")
    elif router[0] == '192.168.234.128':
        tn.write(b"network 20.0.0.0 0.0.0.255 area 0\n") 


    tn.write(b"end\n")

    # Mostrar comando show ip interface brief

    tn.write(b"show ip interface brief\n")
    time.sleep(1)
    output = tn.read_very_eager().decode('ascii')
    print(output)

    tn.write(b"show ip protocols\n")
    time.sleep(1)
    output = tn.read_very_eager().decode('ascii')
    print(output)

    tn.write(b"exit\n")

    # Solicitar el usuario presionar enter para continuar

    input ( f"El router {router[4]} se configuro exitosamente quiere continuar ?")



