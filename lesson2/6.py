import os
from getpass import getpass
from netmiko import ConnectHandler
from time import time

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "lesson6_output.txt"
}

net_connect = ConnectHandler(**cisco4)

print(net_connect.find_prompt())
net_connect.config_mode()
print(net_connect.fimd_prompt())
net_connect.exit_config_mode()
print(net_connect.fimd_prompt())
net_connect.write_channel("disable\n")
time.sleep(2)
print(net_connect.read_channel())
net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()
