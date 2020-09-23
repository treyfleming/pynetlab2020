##Set up J2 Environment
from jinja2 import Template, FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

##Set up Variables

vars_dict = {
    "clock_posix_timezone": "PST",
    "clock_utc_offset": "-8",
    "clock_dst_timezone": "PDT",
    "ntp_server1": "130.126.24.24",
    "ntp_server2": "152.2.21.1",
}


##Loop through a J2 template feeding values from dictionary
for j2_vars in (vars_dict,):
    #Set template file name
    template_file = "5.j2"
    #Load template
    template = env.get_template(template_file)
    #Render template and set to output variable
    output = template.render(**j2_vars)
    print(output)