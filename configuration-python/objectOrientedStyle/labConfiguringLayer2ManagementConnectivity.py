import createBridgeDomainSubnet
import createApplication
import createApplicationEpg
import connectEpgContract
from addPrivateL3Network import input_key_args as input_private_network

from createMo import *


class LabConfiguringLayer2ManagementConnectivity(CreateMo):

    def __init__(self):
        self.description = 'Configuring Out-of-Band Management Access'
        self.tenant_required = True
        self.tenant = 'mgmt'
        self.bridge_domain = {}
        self.application = {}
        self.applied_contract = {}
        super(LabConfiguringLayer2ManagementConnectivity, self).__init__()

    def set_argparse(self):
        super(LabConfiguringLayer2ManagementConnectivity, self).set_argparse()
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

    def run_yaml_mode(self):
        super(LabConfiguringLayer2ManagementConnectivity, self).run_yaml_mode()
        self.bridge_domain = self.args['bridge_domain']
        self.application = self.args['application']
        self.applied_contract = self.args['applied_contract']

    def read_opt_args(self):
        pass

    def wizard_mode_input_args(self):
        self.bridge_domain['name'], self.bridge_domain['subnet_ip'] = createBridgeDomainSubnet.input_key_args()
        self.bridge_domain['private_network'] = input_private_network('')
        self.application = {'name': input_raw_input('Application Profile', required=True),
                            'optional_args': createApplication.input_optional_args(), 'epg': {}}
        self.application['epg']['name'] = createApplicationEpg.input_key_args()
        self.application['epg']['optional_args'] = createApplicationEpg.input_optional_args()
        if is_valid_key(self.application['epg']['optional_args'], 'associated_domain_profile'):
            associated_domain_profile = []
            for i in range(len(self.application['epg']['optional_args']['associated_domain_profile'][0])):
                associated_domain_profile.append(dict({'domain_profile': self.application['epg']['optional_args']['associated_domain_profile'][0][i]}.items() + self.application['epg']['optional_args']['associated_domain_profile'][1][i].items()))
            self.application['epg']['optional_args']['associated_domain_profile'] = associated_domain_profile
        self.applied_contract['name'] = input_raw_input('Contract Name', default='default')
        self.applied_contract['type'] = input_options('Contract Type', 'consumed', ['consumed', 'provided'])



    def main_function(self):

        # create Bridge Domain
        self.check_if_tenant_exist()
        createBridgeDomainSubnet.createBridgeDomainSubnet(self.mo, self.bridge_domain['name'], self.bridge_domain['subnet_ip'], self.bridge_domain['private_network'])

        # # create Application
        fv_ap = createApplication.create_application(self.mo, self.application['name'], optional_args=self.application['optional_args'])
        self.commit_change()

        # create Application EPG
        fv_aepg = createApplicationEpg.create_application_epg(fv_ap, self.application['epg']['name'], optional_args=self.application['epg']['optional_args'])
        self.commit_change()

        # Add Consumedd Contract to the EPG
        connectEpgContract.connect_epg_contract(fv_aepg, self.applied_contract['name'], self.applied_contract['type'])

if __name__ == '__main__':
    mo = LabConfiguringLayer2ManagementConnectivity()
