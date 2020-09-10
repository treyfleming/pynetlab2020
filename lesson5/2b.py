##Set up J2 Environment
from jinja2 import Template, FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

##Set up Variables
#Nxos devices are set up as dictionaries

interface = "Ethernet1/1"
bgp_as = 22
nxos1 = {
    "hostname": "nxos1", 
    "interface": interface, 
    "ipv4_address": "10.1.100.1", 
    "ipv4_netmask": "24",
    "bgp_as": bgp_as,
    }
nxos2 = {
    "hostname": "nxos2", 
    "interface": interface, 
    "ipv4_address": "10.1.100.2", 
    "ipv4_netmask": "24",
    "bgp_as": bgp_as,
    }
nxos1["bgp_neighbor"] = nxos2["ipv4_address"]
nxos2["bgp_neighbor"] = nxos1["ipv4_address"]

##Loop through a J2 template feeding values from dictionary
for nxos_j2_vars in (nxos1, nxos2):
    #Set template file name
    template_file = "2b.j2"
    #Load template
    template = env.get_template(template_file)
    #Render template and set to output variable
    output = template.render(**nxos_j2_vars)
    print(output)