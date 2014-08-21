import getopt
from cobra.model.vmm import DomP
from cobra.model.infra import RsVlanNs

from utility import *


def input_key_args(msg='\nPlease input VMM Domian info:'):
    print msg
    args = []
    args.append(get_optional_input("VMM Provider Name (required)", ['VMware(V)', 'Microsoft(M)'], required=True))
    args.append(get_raw_input("VMM Domain Name (required): ", required=True))
    return args

def input_optional_args():
    args = {}
    args['vlan_name'] = get_raw_input('Vlan Name (default: None): ')
    if args['vlan_name'] not in ['None', 'none', 'NONE', '']:
        args['vlan_mode'] = get_optional_input("Vlan Mode (required) ", ['dynamic(d)', 'static(s)'], required=True)
    return args


def create_vmm_domain(modir, vm_provider, vmm_domain_name, **args):
    vmm_provp = modir.lookupByDn('uni/vmmp-' + vm_provider)
    args = args['args_from_CLI'] if 'args_from_CLI' in args.keys() else args
    vmm_domp = DomP(vmm_provp, vmm_domain_name)
    if 'vlan_name' in args.keys() and 'vlan_mode' in args.keys():
        infra_revlanns = RsVlanNs(vmm_domp,tDn='uni/infra/vlanns-[' + args['vlan_name'] + ']-' + args['vlan_mode'])
    elif 'vlan_name' in args.keys() or 'vlan_mode' in args.keys():
        print 'Please specify both [vlan-name] and [vlan-mode]'

    print_query_xml(vmm_provp)
    commit_change(modir, vmm_provp)

if __name__ == '__main__':

    # Obtain the arguments from CLI
    opts = sys.argv[1:]
    opts.reverse()

    # Obtain the key parameters.
    keys = []
    while len(opts) > 0 and opts[len(opts)-1][0] != '-':
        keys.append(opts.pop())
    opts.reverse()
    try:
        host_name, user_name, password, vm_provider, vmm_domain_name = sys.argv[1:6]
    except ValueError:
        print 'Usage:', __file__, '<hostname> <username> <password> <vm_provider> <VMM_domain_name> [-v <vlan-name>] [-m <vlan-mode>]'
        sys.exit()

    # Obtain the optional arguments that with a flag.
    try:
        opts, args = getopt.getopt(opts, 'v:m:',
                                   ['vlan-name=','vlan-mode='])
        optional_args = {}
        for opt, arg in opts:
            if opt in ('-v', '--vlan-name'):
                optional_args['vlan_name'] = arg
            elif opt in ('-m', '--vlan-mode'):
                optional_args['vlan_mode'] = arg

    except getopt.GetoptError:
        host_name, user_name, password = input_login_info()
        vm_provider, vmm_domain_name = input_key_args()
        optional_args = input_optional_args()

    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    if vm_provider not in ['VMware', 'Microsoft']:
        print 'VM provider has to be either be \"VMware\" or \"Microsoft\"'
    else:
        create_vmm_domain(modir, vm_provider, vmm_domain_name, args_from_CLI=optional_args)

    modir.logout()
