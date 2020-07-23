import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco4)
command = 'ping'
output = net_connect.send_command_timing(command,
        strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
        strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("8.8.8.8",
         strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
          strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
          strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
          strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
          strip_command=False, strip_prompt=False)
output += net_connect.send_command_timing("\n",
          strip_command=False, strip_prompt=False)
print(output)
