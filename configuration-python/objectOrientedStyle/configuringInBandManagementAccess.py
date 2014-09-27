import createVlanPool
import createPhysicalDomain
import createAttachableAccessEntityprofile
import createAccessPortPolicyGroup
import configureInterfacePcAndVpc
import createSubnet
import configureInBandEpgDefault
import createNodeManagementAddress

from createMo import *


class Lab7aLayer3External(CreateMo):
    """
    Integrating With VMware
    """
    def __init__(self):
        self.description = 'Integrating With VMware'
        self.tenant_required = True
        self.tenant = 'mgmt'
        super(Lab7aLayer3External, self).__init__()

    def set_argparse(self):
        super(Lab7aLayer3External, self).set_argparse()
        self.parser_cli = self.subparsers.add_parser(
            'cli', help='Not Support.'
        )

    def delete_mo(self):
        print 'Delete method is not supported in this function.'
        sys.exit()

    def set_cli_mode(self):
        pass

    def run_cli_mode(self):
        print 'CLI mode is not supported in this method. Please try Yaml mode.'
        sys.exit()

    def set_wizard_mode(self):
        pass

    def run_wizard_mode(self):
        print 'Wizard mode is not supported in this method. Please try Yaml mode.'
        sys.exit()

    def run_yaml_mode(self):
        super(Lab7aLayer3External, self).run_yaml_mode()
        self.access_port_policy_group = self.args['access_port_policy_group']
        self.attachable_access_entity_profile = self.args['attachable_access_entity_profile']
        self.physical_domain = self.args['physical_domain']
        self.vlan = self.args['vlan']
        self.configure_VLANs_APIC = self.args['configure_VLANs_APIC']
        self.configure_VLANs_VMM = self.args['configure_VLANs_VMM']
        self.bridge_domain = self.args['bridge_domain']
        self.gateway_ip = self.args['gateway_ip']
        self.in_band_epg_default = self.args['in_band_epg_default']
        self.create_node_management_address_apic_inb = self.args['create_node_management_address_apic_inb']
        self.create_node_management_address_switch_inb = self.args['create_node_management_address_switch_inb']

    def read_opt_args(self):
        pass

    def wizard_mode_input_args(self):
        pass

    def main_function(self):

        # create Vlan Pool:
        self.look_up_mo('uni/infra','')
        createVlanPool.create_vlan_pool(self.mo, self.vlan['vlan_name'], self.vlan['vlan_mode'], self.vlan['range_from'], self.vlan['range_to'])
        self.commit_change()

        # create physics domain:
        self.look_up_mo('uni/', '')
        createPhysicalDomain.create_physical_domain(self.mo, self.physical_domain, vlan_pool=self.vlan['vlan_name'], vlan_mode=self.vlan['vlan_mode'])
        self.commit_change()

        # create Attachable Access Entity Profile:
        self.look_up_mo('uni/infra','')
        createAttachableAccessEntityprofile.create_attachable_access_entity_profile(self.mo, self.attachable_access_entity_profile, domain_profiles=[self.physical_domain])
        self.commit_change()

        # create Access Port Policy Group:
        self.look_up_mo('uni/infra/funcprof/', '')
        createAccessPortPolicyGroup.create_access_port_port_policy_group(self.mo, self.access_port_policy_group, entity_profile=self.attachable_access_entity_profile)
        self.commit_change()

        # create a new profile and configure VLANs for the APIC
        # and configure the VLANs for the VMM server ports.
        self.look_up_mo('uni/infra', '')
        configureInterfacePcAndVpc.configure_interface_pc_and_vpc(self.mo, self.configure_VLANs_APIC['switch_profile'], self.configure_VLANs_APIC['switches'], self.configure_VLANs_APIC['interface_type'], self.configure_VLANs_APIC['interface_ports'], self.configure_VLANs_APIC['interface_selector'], self.access_port_policy_group)
        self.commit_change()
        configureInterfacePcAndVpc.configure_interface_pc_and_vpc(self.mo, self.configure_VLANs_VMM['switch_profile'], self.configure_VLANs_VMM['switches'], self.configure_VLANs_VMM['interface_type'], self.configure_VLANs_VMM['interface_ports'], self.configure_VLANs_VMM['interface_selector'], self.access_port_policy_group)
        self.commit_change()

        # create subnet
        self.look_up_mo('uni/tn-'+self.tenant+'/BD-', self.bridge_domain)
        createSubnet.create_subnet(self.mo, self.gateway_ip)
        self.commit_change()

        # configure In-Band Epg Default:
        self.look_up_mo('uni/tn-'+self.tenant+'/mgmtp-default','')
        configureInBandEpgDefault.configureIn_band_epg_default(self.mo, self.in_band_epg_default['name'], optional_args=self.in_band_epg_default)

        # create Node Management Address Apic
        self.look_up_mo('uni/infra/funcprof','')
        createNodeManagementAddress.create_node_management_address(self.mo, self.create_node_management_address_apic_inb['name'], optional_args=self.create_node_management_address_apic_inb)
        if is_valid_key(self.create_node_management_address_apic_inb, 'in_band_management_epg'):
            self.commit_change()
            self.check_if_tenant_exist()
            createNodeManagementAddress.create_ip_address_pool(self.mo, self.create_node_management_address_apic_inb['name'], optional_args=self.create_node_management_address_apic_inb)
        if is_valid_key(self.create_node_management_address_apic_inb, 'fabric_nodes_id'):
            self.commit_change()
            self.look_up_mo('uni/infra', '')
            createNodeManagementAddress.create_infra_nodes(self.mo, self.create_node_management_address_apic_inb['name'], self.create_node_management_address_apic_inb['fabric_nodes_id'])
        self.commit_change()

        # create Node Management Address Switch
        self.look_up_mo('uni/infra/funcprof','')
        createNodeManagementAddress.create_node_management_address(self.mo, self.create_node_management_address_switch_inb['name'], optional_args=self.create_node_management_address_switch_inb)
        if is_valid_key(self.create_node_management_address_switch_inb, 'in_band_management_epg'):
            self.commit_change()
            self.check_if_tenant_exist()
            createNodeManagementAddress.create_ip_address_pool(self.mo, self.create_node_management_address_switch_inb['name'], optional_args=self.create_node_management_address_switch_inb)
        if is_valid_key(self.create_node_management_address_switch_inb, 'fabric_nodes_id'):
            self.commit_change()
            self.look_up_mo('uni/infra', '')
            createNodeManagementAddress.create_infra_nodes(self.mo, self.create_node_management_address_switch_inb['name'], self.create_node_management_address_switch_inb['fabric_nodes_id'])
        self.commit_change()


if __name__ == '__main__':
    mo = Lab7aLayer3External()