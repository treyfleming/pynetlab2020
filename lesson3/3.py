import json
from pprint import pprint

input_file = '3_input.json'

with open(input_file, 'r') as f:
    json_data = json.load(f)

ipaddr_v4 = []
ipaddr_v6 = []

for intf, ipinfo_dict in json_data.items():
    for ipver, ip_addr_prefix in ipinfo_dict.items():
        for ip_addr, prefix_dict in ip_addr_prefix.items():
            prefix_length = prefix_dict['prefix_length']
            if ipver == "ipv4":
                ipaddr_v4.append("{}/{}".format(ip_addr, prefix_length))
            elif ipver == "ipv6":
                ipaddr_v6.append("{}/{}".format(ip_addr, prefix_length))

print("\n IPv4 Addresses: {}\n".format(ipaddr_v4))
print("\n IPv6 Addresses: {}\n".format(ipaddr_v6))