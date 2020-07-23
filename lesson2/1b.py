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
output = net_connect.send_command(command, expect_string=r'Protocol',
        strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Target',
        strip_command=False, strip_prompt=False)
output += net_connect.send_command("8.8.8.8", expect_string=r'Repeat',
         strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Datagram',
          strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Timeout',
          strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Extended',
          strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Sweep',
          strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'#',
          strip_command=False, strip_prompt=False)
net_connect.disconnect()
print(output)
