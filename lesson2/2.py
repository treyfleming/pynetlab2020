import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**nxos2)
command = 'show lldp neighbors'
start_time = datetime.now()
output = net_connect.send_command(command)
end_time = datetime.now()
print('#' * 80)
print(output)
print('#' * 80)
print("\n\nExecution time:{}".format(end_time - start_time))
print()
start_time = datetime.now()
output = net_connect.send_command(command, delay_factor=8)
end_time = datetime.now()
print('#' * 80)
print(output)
print('#' * 80)
print("\n\nExecution time:{}".format(end_time - start_time))
print()
net_connect.disconnect()
