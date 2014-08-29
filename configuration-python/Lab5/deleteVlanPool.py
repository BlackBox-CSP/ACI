from cobra.model.fvns import VlanInstP
from createVlanPool import input_key_args

from utility import *


def delete_vlan_pool(modir, vlan_name, allocation_mode):

    # Query to the VLAN pool.
    fvns_vlaninstp = modir.lookupByDn('uni/infra/vlanns-' + vlan_name + '-' + allocation_mode)

    if isinstance(fvns_vlaninstp, VlanInstP):
        # delete the VLAN
        fvns_vlaninstp.delete()
    else:
        print 'There is no VLAN', vlan_name, '(', allocation_mode, ').'
        return

    print_query_xml(fvns_vlaninstp)
    commit_change(modir, fvns_vlaninstp)

if __name__ == '__main__':

    # Obtain the key parameters.
    key_args = [{'name': 'vlan', 'help': 'VLAN name'},
                {'name': 'allocation', 'help': 'Allocation Mode'}
    ]

    try:
        host_name, user_name, password, args = set_cli_argparse('Delete a VLAN pool.', key_args)
        vlan_name = args.pop('vlan')
        allocation_mode = args.pop('allocation')

    except SystemExit:

        if check_if_requesting_help(sys.argv):
            sys.exit('Help Page')

        if len(sys.argv)>1:
            print 'Invalid input arguments.'

        host_name, user_name, password = input_login_info()
        vlan_name, allocation_mode = input_key_args(from_delete_function=True)

    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    if allocation_mode.lower() not in ['dynamic', 'static']:
        print 'VM provider has to be either be \"dynamic\" or \"static\"'
    else:
        delete_vlan_pool(modir, vlan_name, allocation_mode.lower())

    modir.logout()


