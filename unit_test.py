from drawio_network_plot import NetPlot

''' 
Testing topology is mafde of :
	- 2 routers
	- 2 Core/Spine Switches
	- 2 Out of path firewalls
	- 4 Leaf/Access switches
	- 16 Server
'''
device_list = [
				# Routers
				{'nodeName' : 'Router_1','nodeType' : 'router','nodeDescription' : 'External Peering Provider 1'},
				{'nodeName' : 'Router_2','nodeType' : 'router','nodeDescription' : 'External Peering Provider 2'},
				# Core
				{'nodeName' : 'Core_switch_1','nodeType' : 'l3_switch','nodeDescription' : 'Spine Switch 01'},
				{'nodeName' : 'Core_switch_2','nodeType' : 'l3_switch','nodeDescription' : 'Spine Switch 02'},
				# Firewalls
				{'nodeName' : 'FW_1','nodeType' : 'firewall','nodeDescription' : 'Firewall 01'},
				{'nodeName' : 'FW_2','nodeType' : 'firewall','nodeDescription' : 'Firewall 02'},
				# Leafs
				{'nodeName' : 'TOR_1','nodeType' : 'l2_switch','nodeDescription' : 'Leaf Switch 01'},
				{'nodeName' : 'TOR_2','nodeType' : 'l2_switch','nodeDescription' : 'Leaf Switch 02'},
				{'nodeName' : 'TOR_3','nodeType' : 'l2_switch','nodeDescription' : 'Leaf Switch 03'},
				{'nodeName' : 'TOR_4','nodeType' : 'l2_switch','nodeDescription' : 'Leaf Switch 04'},
			 	# Servers 
			 	{'nodeName' : 'Server_1','nodeType' : 'server','nodeDescription' : 'Server 1'},
				{'nodeName' : 'Server_2','nodeType' : 'server','nodeDescription' : 'Server 2'},
				{'nodeName' : 'Server_3','nodeType' : 'server','nodeDescription' : 'Server 3'},
				{'nodeName' : 'Server_4','nodeType' : 'server','nodeDescription' : 'Server 4'},
				{'nodeName' : 'Server_5','nodeType' : 'server','nodeDescription' : 'Server 5'},
				{'nodeName' : 'Server_6','nodeType' : 'server','nodeDescription' : 'Server 6'},
				{'nodeName' : 'Server_7','nodeType' : 'server','nodeDescription' : 'Server 7'},
				{'nodeName' : 'Server_8','nodeType' : 'server','nodeDescription' : 'Server 8'},
				{'nodeName' : 'Server_9','nodeType' : 'server','nodeDescription' : 'Server 9'},
				{'nodeName' : 'Server_10','nodeType' : 'server','nodeDescription' : 'Server 10'},
				{'nodeName' : 'Server_11','nodeType' : 'server','nodeDescription' : 'Server 11'},
				{'nodeName' : 'Server_12','nodeType' : 'server','nodeDescription' : 'Server 12'},
				{'nodeName' : 'Server_13','nodeType' : 'server','nodeDescription' : 'Server 13'},
				{'nodeName' : 'Server_14','nodeType' : 'server','nodeDescription' : 'Server 14'},
				{'nodeName' : 'Server_15','nodeType' : 'server','nodeDescription' : 'Server 15'},
				{'nodeName' : 'Server_16','nodeType' : 'server','nodeDescription' : 'Server 16'},
			  ]


connection_list = [
					# Router to Core
					{'sourceNodeID' : 'Router_1','destinationNodeID' : 'Core_switch_1'},
					{'sourceNodeID' : 'Router_1','destinationNodeID' : 'Core_switch_2'},
					{'sourceNodeID' : 'Router_2','destinationNodeID' : 'Core_switch_1'},
					{'sourceNodeID' : 'Router_2','destinationNodeID' : 'Core_switch_2'},
					# Core to FW 
					{'sourceNodeID' : 'Core_switch_1','destinationNodeID' : 'FW_1'},
					{'sourceNodeID' : 'Core_switch_2','destinationNodeID' : 'FW_2'},
					# Core to TOR 
					{'sourceNodeID' : 'Core_switch_1','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Core_switch_1','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Core_switch_1','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Core_switch_1','destinationNodeID' : 'TOR_4'},
					{'sourceNodeID' : 'Core_switch_2','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Core_switch_2','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Core_switch_2','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Core_switch_2','destinationNodeID' : 'TOR_4'},
					# TOR to Server 
					{'sourceNodeID' : 'Server_1','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Server_2','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Server_3','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Server_4','destinationNodeID' : 'TOR_4'},
					{'sourceNodeID' : 'Server_5','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Server_6','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Server_7','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Server_8','destinationNodeID' : 'TOR_4'},
					{'sourceNodeID' : 'Server_9','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Server_10','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Server_11','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Server_12','destinationNodeID' : 'TOR_4'},
					{'sourceNodeID' : 'Server_13','destinationNodeID' : 'TOR_1'},
					{'sourceNodeID' : 'Server_14','destinationNodeID' : 'TOR_2'},
					{'sourceNodeID' : 'Server_15','destinationNodeID' : 'TOR_3'},
					{'sourceNodeID' : 'Server_16','destinationNodeID' : 'TOR_4'},				
				]


x = NetPlot()
# x.addNode(nodeName='Router_17',nodeType='router')
# x.addNode(nodeName='Router_18',nodeType='router')
# x.addLink('Router_17','Router_18')
# x.addLink('Router_17','Router_1')
x.addNodeList(device_list)
x.addLinkList(connection_list)
print(x.display_xml())




















