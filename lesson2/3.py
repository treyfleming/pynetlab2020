import os
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco4)

print()
my_cmnds = ["show version", "show lldp neighbors"]
for cmd in my_cmnds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print("#" * 80)
    print(cmd)
    print("#" *80)
    pprint(output)
    print("#" *80)
    print()

    if cmd == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Port: {}".format(output[0]['neighbor_interface']))
print()
net_connect.disconnect()
