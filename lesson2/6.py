import os
from getpass import getpass
from netmiko import ConnectHandler
from time import sleep

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


print("\n Print prompt: ")
print(net_connect.find_prompt())

print("\n Enter config mode, print prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())

print("\n Exit config mode, print prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print("\n Exit priveleged mode (disable), print prompt: ")
net_connect.write_channel("disable\n")
sleep(2)
print(net_connect.read_channel())

print("\n Enter priveleged mode (enable), print prompt: ")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()
