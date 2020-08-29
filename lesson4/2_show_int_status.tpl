Value PORT_NAME (\S+)
Value PORT_STATUS (\S+)
Value VLAN_ID (\d+)
Value PORT_SPEED (\S+)
Value PORT_DUPLEX (\S+)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTable

ShowIntTable
  ^${PORT_NAME}\s+${PORT_STATUS}\s+${VLAN_ID}\s+${PORT_SPEED}\s+${PORT_DUPLEX}\s+${PORT_TYPE}\s*$$ -> Record

EOF

####
#FSM Table:
#['PORT_NAME', 'STATUS', 'VLAN', 'DUPLEX', 'SPEED', 'PORT_TYPE']
#['Gi0/1/0','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/1','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/2','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/3','notconnect','1','auto','auto','10/100/1000BaseTX']
#
#
#
#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
