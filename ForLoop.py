filename = "routers.txt"
with open(filename) as f:
    routers = [line.strip().split(",") for line in f]

for router in routers:
    print(router[0])
    if router[0] == '192.168.234.129' or router[0] == "192.168.234.128":
        continue
    print(router[0])
else:
    print("This value is skipped")

