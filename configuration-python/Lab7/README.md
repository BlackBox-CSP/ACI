Lab7
====================

For beginner user, you can simply run the code directly:
eg: python createTenant.py
Then you just need to follow the Wizard to finish the configuration.

====================

For advanced user, you could put all the key arguments and optional arguments when you call the python code.
The format of the key arguments and optional argument for all the codes are list as below:

--------------------------------------------------------------------

associateL3OutsideNetworkToBD.py: to associate the L3 Outside network to a Bridge Domain.
usage:
python associateL3OutsideNetworkToBD.py <hostname> <username> <password> <tenant_name> <bridge_domain> <external_network_name>
python associateL3OutsideNetworkToBD.py 172.22.233.207 admin Cisco123 ACILab ACILab_BD1 ACILab_VRF

--------------------------------------------------------------------

configPrivateL3NetworkDefaultTimers.py: Set Setting for Private Network
usage:
python configPrivateL3NetworkDefaultTimers.py <hostname> <username> <password> <tenant_name> <private_network> [-B <BGP_timer>] [-O <OSPF_timer>] [-e End <point_retention_policy>] [-m <monitoring_olicy>]
python configPrivateL3NetworkDefaultTimers.py 172.22.233.207 admin Cisco123 ACILab ACILab_VRF -O default

--------------------------------------------------------------------

createBgpRouteReflector.py: Set Setting for Private Network
usage:
python createBgpRouteReflector.py <hostname> <username> <password> <spin_id>
python createBgpRouteReflector.py 172.22.233.207 admin Cisco123 102

--------------------------------------------------------------------

createExternalNetwork.py: Set Setting for Private Network
usage:
python createExternalNetwork.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <external_network_name> [-Q <QoS_class>] [-s <subnet_ip>] 
python createExternalNetwork.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out L3-Out-EPG -Q unspecified -s 0.0.0.0/0

--------------------------------------------------------------------

createInterfaceProfile.py: Set Setting for Private Network
usage:
python createInterfaceProfile.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <interface_name>
python createInterfaceProfile.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out L3-OSPF-Leaf2

--------------------------------------------------------------------

createL3EpgConsumerContract.py: Set Setting for Private Network
usage:
python createL3EpgConsumerContract.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <external_network_name> <contract_name> [-Q <QoS_class>]
python createL3EpgConsumerContract.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out L3-Out-EPG default -Q unspecified

--------------------------------------------------------------------

createL3EpgProviderContract.py: Set Setting for Private Network
usage:
python createL3EpgProviderContract.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <external_network_name> <contract_name> [-Q <QoS_class>] [-m <match_type>]
python createL3EpgProviderContract.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out L3-Out-EPG default -Q unspecified -m AtleastOne

--------------------------------------------------------------------

createNodes.py: Set Setting for Private Network
usage:
python createNodes.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name> <leaf_id> <router_id>
python createNodes.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2 102 1.0.0.2

--------------------------------------------------------------------

createNodesAndInterfacesProfile.py: Set Setting for Private Network
usage:
python createNodesAndInterfacesProfile.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name> [-D <target_DSCP>]
python createNodesAndInterfacesProfile.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2 -D 1

--------------------------------------------------------------------

createPodPolicyGroup.py: Set Setting for Private Network
usage:
python createPodPolicyGroup.py <hostname> <username> <password> <policy_group_name> [-d Date Time_policy?] [-I ISIS_policy?] [-C COOP_group_poicy?] [-B BGP_route_reflector_policy?] [-c communication_policy?] [-S SNMP_policy] 
python createPodPolicyGroup.py 172.22.233.207 admin Cisco123 PodPolicy -B

--------------------------------------------------------------------

createRoutedInterfaceProfile.py: Set Setting for Private Network
usage:
python createRoutedInterfaceProfile.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name> <interface_name> <leaf_id> <eth_num> <ip_address> [-M <MTU>] [-D <target_DSCP>]
python createRoutedInterfaceProfile.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2 L3-OSPF-Leaf2 102 1/1 30.30.30.1/24 -M 1500

--------------------------------------------------------------------

createRoutedOutside.py: Set Setting for Private Network
usage:
python createRoutedOutside.py <hostname> <username> <password> <tenant_name> <routed_outside_name> [-n <private_network>] [-t <tags>] [-B BGP?] [-O OSPF?] [-i OSPF_id]
python createRoutedOutside.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out -n ACILab_VRF -O -i 1

--------------------------------------------------------------------

deleteBgpRouteReflector.py: to delete a bridge domain.
usage:
python deleteBgpRouteReflector.py <hostname> <username> <password> <spine_id>
python deleteBgpRouteReflector.py 172.22.233.207 admin Cisco123 102

--------------------------------------------------------------------
deleteExternalNetwork.py: to delete a bridge domain.
usage:
python deleteExternalNetwork.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <external_network_name>
python deleteExternalNetwork.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out L3-Out-EPG

--------------------------------------------------------------------

deleteNodes.py: to delete a bridge domain.
usage:
python deleteNodes.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name> <leaf_id>
python deleteNodes.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2 102

--------------------------------------------------------------------

deleteNodesAndInterfacesProfile.py: to delete a bridge domain.
usage:
python deleteNodesAndInterfacesProfile.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name>
python deleteNodesAndInterfacesProfile.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2

--------------------------------------------------------------------

deletePodPolicyGroup.py: to delete a bridge domain.
usage:
python deletePodPolicyGroup.py <hostname> <username> <password> <policy_name>
python deletePodPolicyGroup.py 172.22.233.207 admin Cisco123 PodPolicy

--------------------------------------------------------------------

deleteRoutedInterfaceProfile.py: to delete a bridge domain.
usage:
python deleteRoutedInterfaceProfile.py <hostname> <username> <password> <tenant_name> <routed_outside_name> <node_profile_name> <interface_name> <leaf_id> <eth_num> 
python deleteRoutedInterfaceProfile.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out Border-Leaf2 L3-OSPF-Leaf2 102 1/1

--------------------------------------------------------------------

deleteRoutedOutside.py: to delete a bridge domain.
usage:
python deleteRoutedOutside.py <hostname> <username> <password> <tenant_name> <routed_outside_name>
python deleteRoutedOutside.py 172.22.233.207 admin Cisco123 ACILab ACILab-L3-Out

--------------------------------------------------------------------

deselectPodPolicy.py: to delete a bridge domain.
usage:
python deselectPodPolicy.py <hostname> <username> <password> 
python deselectPodPolicy.py 172.22.233.207 admin Cisco123

--------------------------------------------------------------------

disassociateL3OutsideNetworkToBD.py: to delete a bridge domain.
usage:
python disassociateL3OutsideNetworkToBD.py <hostname> <username> <password> <tenant_name> <bridge_domain> <routed_outside_name> 
python disassociateL3OutsideNetworkToBD.py 172.22.233.207 admin Cisco123 ACILab ACILab_BD1 ACILab-L3-Out

--------------------------------------------------------------------

lab7A_Layer3External.py: a implement code that utilize all the codes under this folder in order to accomplish the first one third tasks in Lab7 in Lab Guide (version 1.19)
usage:
python lab2_CreateTenant.py <hostname> <username> <password> <pod_policy>
python lab2_CreateTenant.py 172.22.233.207 admin Cisco123 PodPolicy

--------------------------------------------------------------------

lab7B_RoutedL3ExternalNetwork.py: a implement code that utilize all the codes under this folder in order to accomplish the second one third tasks in Lab7 in Lab Guide (version 1.19)
usage:
python lab2_CreateTenant.py <hostname> <username> <password> <tenant_name>
python lab2_CreateTenant.py 172.22.233.207 admin Cisco123 ACILab

--------------------------------------------------------------------

lab7C_SetupL3OutNetworkAndBD.py: a implement code that utilize all the codes under this folder in order to accomplish the last one third tasks in Lab7 in Lab Guide (version 1.19)
usage:
python lab2_CreateTenant.py <hostname> <username> <password> <tenant_name>
python lab2_CreateTenant.py 172.22.233.207 admin Cisco123 ACILab

--------------------------------------------------------------------

lab7A_Wizard_Layer3External.py:  a step by step Wizard that helps user to accomplish the tasks in Lab3 in Lab Guide (version 1.19)
lab7B_Wizard_RoutedL3ExternalNetwork.py:  a step by step Wizard that helps user to accomplish the tasks in Lab3 in Lab Guide (version 1.19)
lab7C_Wizard_setupL3OutNetworkAndBD.py:  a step by step Wizard that helps user to accomplish the tasks in Lab3 in Lab Guide (version 1.19)

