##Set up J2 Environment
from jinja2 import Template, FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

##Set up Variables

vrf_dict = [
     {
        "vrf_name": "blue",
        "vrf_rd": "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },
    {
        "vrf_name": "red",
        "vrf_rd": "200:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },

    {
        "vrf_name": "green",
        "vrf_rd": "300:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },

    {
        "vrf_name": "yellow",
        "vrf_rd": "400:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },

    {
        "vrf_name": "violet",
        "vrf_rd": "500:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },
]

##This sets the j2_vars to be passed into the J2 template as a dict. 
# The key is "suck_balls", which is referenced from within the J2 tempate.
# The value is the 'my_dict' variable above

j2_vars = {"suck_balls": vrf_dict}


##Loop through a J2 template feeding values from dictionary
#Set template file name
template_file = "4.j2"
#Load template
template = env.get_template(template_file)
#Render template and set to output variable
output = template.render(**j2_vars)
print(output)