import os
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

input_file = '5_input.yml'

with open(input_file) as f:
    yaml_data = yaml.safe_load(f)

cisco4 = yaml_data['cisco4']

net_connect = ConnectHandler(**cisco4)

sh_run = net_connect.send_command('show running-config')

my_config = CiscoConfParse(sh_run.splitlines())

intfs = my_config.find_objects_w_child(r"^interface", r"^\s+ip address")

print()

for intf in intfs:
    print("Interface Line: {}".format(intf.text))
    ip_address = intf.re_search_children(r"ip address")[0].text
    print("IP Address Line: {}".format(ip_address))
    print()
print()

