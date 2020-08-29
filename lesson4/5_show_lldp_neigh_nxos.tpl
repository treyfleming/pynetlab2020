Value DEVICE_ID (\S+)
Value LOCAL_INTF (\S+\d\/\d)
Value CAPABILITY (\S+)
Value PORT_ID (\S+\d\/\d)

Start
  ^Device ID.*Port ID*.*$$ -> LLDP

LLDP
  ^${DEVICE_ID}\s+${LOCAL_INTF}\s+\d+\s+${CAPABILITY}\s+${PORT_ID}\s+ -> Record

#Parse the 'show lldp neighbors' output from nxos1 (see link below). 
#From this output use TextFSM to extract the Device ID, Local Intf, Capability, and Port ID.
#
#
#Capability codes:
#  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
#  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
#Device ID                         Local Intf          Hold-time   Capability  Port ID     
#nxos2.twb-tech.com                Eth2/1              120          BR          Eth2/1      
#nxos2.twb-tech.com                Eth2/2              120          BR          Eth2/2      
#nxos2.twb-tech.com                Eth2/3              120          BR          Eth2/3      
#nxos2.twb-tech.com                Eth2/4              120          BR          Eth2/4      
#Total entries displayed: 4
