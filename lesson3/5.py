import os
import yaml
from netmiko import ConnectHandler
from getpass import getpass

input_file = '5_input.yml'

with open(input_file) as f:
    yaml_data = yaml.safe_load(f)

cisco3 = yaml_data['cisco3']

net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()

