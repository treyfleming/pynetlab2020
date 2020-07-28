from pprint import pprint

cisco3 = {'dev_name': 'cisco3', 'hostname': 'cisco3.lasthop.io'}

cisco4 = {'dev_name': 'cisco4', 'hostname': 'cisco4.lasthop.io'}

arista1 = {'dev_name': 'arista1', 'hostname': 'arista1.lasthop.io'}

arista2 = {'dev_name': 'arista2', 'hostname': 'arista2.lasthop.io'}

my_devices = [cisco3, cisco4, arista1, arista2]

for device in my_devices:
    device['username'] = 'admin'
    device['password'] = 'cisco1234'

print()
pprint(my_devices)
print()