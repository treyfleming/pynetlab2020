import re
import os
from pprint import pprint

mydata = """
    Protocol  Address      Age  Hardware Addr   Type  Interface
    Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
    Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
    Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
    Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
    Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
mydata = mydata.strip()
my_list = mydata.splitlines()

new_list = []

for list_entry in my_list:
    if re.search(r"^Protocol.*Interface", list_entry):
        continue
    _, ip_addr, _, mac_addr, _, intf = list_entry.split()
    my_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "intf": intf}
    new_list.append(my_dict)

print()
pprint(new_list)
print()