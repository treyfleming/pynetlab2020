#### Lesson 7 - Pulling BGP config and returning neighbors / remote AS numbers
#7. You have the following BGP configuration from a Cisco IOS-XR router:
#router bgp 44
# bgp router-id 10.220.88.38
# address-family ipv4 unicast
# !
# neighbor 10.220.88.20
#  remote-as 42
#  description pynet-rtr1
#  address-family ipv4 unicast
#   route-policy ALLOW in
#   route-policy ALLOW out
#  !
# !
# neighbor 10.220.88.32
#  remote-as 43
#  address-family ipv4 unicast
#   route-policy ALLOW in
#   route-policy ALLOW out
#
#From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.
#
#Your output should look similar to the following. Use ciscoconfparse to accomplish this.
#​BGP Peers: 
#[('10.220.88.20', '42'), ('10.220.88.32', '43')]
####
import os
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse


# Define BGP Config
bgp_conf = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

#Pass config variable into CiscConfParse - Needs to be a list so need .splitlines()
parsed_config = CiscoConfParse(bgp_conf.splitlines())

#Create empty list for BGP peers.
bgp_peers = []

#Find BGP neighbors under 'router bgp xxx' configuration
bgp_neighbors = parsed_config.find_objects_w_parents(r"^router\sbgp\s\d*", r"^\sneighbor .*")

#print(bgp_neighbors)

for neighbor in bgp_neighbors: #Iterate through "neighbor" statements under 'router bgp config
    _, neighbor_ip = neighbor.text.split() # Input text = 'neighbor xxx.xxx.xxx.xxx - _ sets a 'blank variable to store 'neighbor''
    for child in neighbor.children: #Iterate through child configs under "neighbor"
        if "remote-as" in child.text: #Seek and iterate through remote-as statements
            _, remote_as = child.text.split()
    #Add BGP Peers to blank list
    bgp_peers.append((neighbor_ip, remote_as)) #Need double parenthesis because passing two arguments

#Print desired output
print()
print("BGP Peers: ")
print(bgp_peers)
print()

#Reference configuration: https://github.com/ktbyers/pyplus_course/blob/master/class3/exercises/confparse_ex7.py