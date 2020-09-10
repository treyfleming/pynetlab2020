##Set up J2 Environment
from jinja2 import Template, FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

##Set up Variables

vrf100 = {
    "vrf_name": "blue",
    "vrf_rd": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": True,
}


##Loop through a J2 template feeding values from dictionary
for vrf_j2_vars in (vrf100,):
    #Set template file name
    template_file = "3.j2"
    #Load template
    template = env.get_template(template_file)
    #Render template and set to output variable
    output = template.render(**vrf_j2_vars)
    print(output)