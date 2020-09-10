##Set up J2 Environment
import time
import re

from jinja2 import Template, FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from getpass import getpass
from netmiko import ConnectHandler

##Import variables file
from variables import nxos1, nxos2

##Set up Main function
if __name__ == "__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./templates")

    ##Set up Variables
    #Nxos devices are set up as dictionaries
    template_file = "2c.j2"
    interface = "Ethernet1/1"
    bgp_as = 22

    nxos1_vars = {
        "hostname": "nxos1", 
        "interface": interface, 
        "ipv4_address": "10.1.100.1", 
        "ipv4_netmask": "24",
        "bgp_as": bgp_as,
    }

    nxos2_vars = {
        "hostname": "nxos2", 
        "interface": interface, 
        "ipv4_address": "10.1.100.2", 
        "ipv4_netmask": "24",
        "bgp_as": bgp_as,
    }
    nxos1_vars["bgp_neighbor"] = nxos2_vars["ipv4_address"]
    nxos2_vars["bgp_neighbor"] = nxos1_vars["ipv4_address"]

    ##Add J2 vars to be included with netmiko device dictionary
    nxos1["j2_vars"] = nxos1_vars
    nxos2["j2_vars"] = nxos2_vars

    print()
    ##Loop through a J2 template feeding values from dictionary
    for device in (nxos1, nxos2):
        ## Create a copy because there's going to be some modification shit
        tmp_device = device.copy()
        j2_vars = tmp_device.pop("j2_vars")
        template = env.get_template(template_file)
        cfg = template.render(**j2_vars)
        hostname = device["j2_vars"]["hostname"]
        print(f" {hostname} ".center(80, "#"))
        print(f"\n>>> Template output {hostname}")
        print(cfg)
        cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]
       
        ##Do some Netmiko stuff
        net_connect = ConnectHandler(**tmp_device)
        #Store the SSH connection for later so there's no need to reconnect
        device["ssh_conn"] = net_connect
        print(f">>> Configuring {hostname}")
        output = net_connect.send_config_set(cfg_lines)
        print(output)
        print("\n\n")
    
    #Pause to give BGP time to come alive
    sleep_time = 15
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)

    print("\n\n")
    print(">>> Testing ping and BGP")
    
    ### Test Ping and BGP
    for device in (nxos1, nxos2):
        net_connect = device["ssh_conn"]
        remote_ip = device["j2_vars"]["bgp_neighbor"]
        
        #Test ping
        output = net_connect.send_command(f"ping {remote_ip}")
        print(output)
        if "64 bytes from" not in output:
            print("\n Ping failed!!!")
        print("\n\n")

        #Test BGP
        bgp_verify = f"show ip bgp summary | include {remote_ip}"
        output = net_connect.send_command(bgp_verify)
        # Retrieve the State/PfxRdd field which is the last field
        match = re.search(r"\s+(\S+)\s*$", output)
        prefix_received = match.group(1)
        try:
            # if this is an integer, bgp is up and you're receiving prefixes
            int(prefix_received)
            print(
                f"BGP reached the established state. Prefixes received {prefix_received}")

        except ValueError:
                print("BGP failed to reach the established state")
    # Kill connection
    for device in (nxos1, nxos2):
        net_connect = device["ssh_conn"]
        net_connect.disconnect()
    print("\n\n")

