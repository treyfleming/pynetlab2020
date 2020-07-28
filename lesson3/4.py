import json
from pprint import pprint

input_file = '4_input.json'

with open(input_file, 'r') as f:
    json_data = json.load(f)

arp_dict = {}                                                                                                                                       

arp_entries = json_data['ipV4Neighbors']                                                                                                            
for arp_entry in arp_entries: 
    ip_addr = arp_entry['address'] 
    hw_addr = arp_entry['hwAddress'] 
    arp_dict[ip_addr] = hw_addr

print()
pprint(arp_dict)
print()
