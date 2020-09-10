### Set up device variables for netmiko connections
##
## import os and getpass modules into this file. That shit is needed
import os
from getpass import getpass

##Set up password variable to reference below: if "PYNET_PASSWORD" is set in ENV, use that. Otherwise prompt
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

###Set up Connection Variables
nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    }


nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}