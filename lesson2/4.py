import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

start_time = datetime.now()
cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco3)

print()
my_cmnds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
output = net_connect.send_config_set(my_cmnds)
print()
print("#" * 80)
print("Config Change:")
print(output)
print("#" *80)
print()

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful")
    print("\n\nPing Output: {}".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()
print("Total Execution time: {}\n".format( end_time - start_time))