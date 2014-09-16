import addFabricNode
from createMo import *

class Lab1FabricDiscovery(CreateMo):
    """
    Discover switches and spines
    """
    def __init__(self):
        self.description = 'Discovery all the switches and spines'
        self.fabricNodes = []
        super(Lab1FabricDiscovery, self).__init__()

    def set_argparse(self):
        super(Lab1FabricDiscovery, self).set_argparse()
        self.parser_cli = self.subparsers.add_parser(
            'cli', help='Not Support.'
        )

    def set_cli_mode(self):
        pass

    def run_cli_mode(self):
        print 'CLI mode is not supported in this method. Please try Yaml mode or Wizard mode.'
        sys.exit()

    def run_yaml_mode(self):
        super(Lab1FabricDiscovery, self).run_yaml_mode()
        self.fabricNodes = self.args['fabric_nodes']

    def run_wizard_mode(self):
        super(Lab1FabricDiscovery, self).run_wizard_mode()
        fabric_nodes = add_mos('Add a Fabric Node', addFabricNode.input_key_args)
        for fabric_node in fabric_nodes:
            args = {'serial_number': fabric_node['key_args'][0],
                    'node_id': fabric_node['key_args'][1],
                    'node_name': fabric_node['key_args'][2]}
            self.fabricNodes.append(args)
        print self.fabricNodes

    def lab1FabricDiscovery(self):
        parent_mo = self.check_if_mo_exist('uni/controller/nodeidentpol', description='Fabric Node')
        for fabricNode in self.fabricNodes:
            addFabricNode.add_fabric_node(parent_mo, fabricNode['serial_number'], fabricNode['node_id'], fabricNode['node_name'])

if __name__ == '__main__':
    mo = Lab1FabricDiscovery()