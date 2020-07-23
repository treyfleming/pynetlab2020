import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}
config_file = "config_changes.txt"
for device in (nxos1, nxos2)
net_connect = ConnectHandler(**device)
output = net_connect.send_config_from_file(config_file)
output += net_connect.save_config()
print()
print(output)
print()