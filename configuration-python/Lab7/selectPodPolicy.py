from cobra.model.fabric import RsPodPGrp

from utility import *


def input_key_args(msg='\nPlease Select the Policy Group:'):
    print msg
    return get_raw_input("Fabric Policy Group Name (required): ", required=True)


def select_pod_policy(modir, frabic_policy_group):
    # Query to Pod Selector
    bgp_pods = modir.lookupByDn('uni/fabric/podprof-default/pods-default-typ-ALL')
    # Set Pod Selector
    bgp_rspodpgrp = RsPodPGrp(bgp_pods, tDn='uni/fabric/funcprof/podpgrp-' + frabic_policy_group)

    print_query_xml(bgp_pods)
    commit_change(modir, bgp_pods)

if __name__ == '__main__':

    # Obtain the key parameters.
    try:
        key_args = [{'name': 'policy_group', 'help': 'The Selected Policy Group name'}]
        host_name, user_name, password, args = set_cli_argparse('Select a Pod Policy Group for Fabric Policy Group.', key_args)
        frabic_policy_group = args.pop('policy_group')

    except: #?error

        if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
            sys.exit('Help Page')

        host_name, user_name, password = input_login_info()
        frabic_policy_group = input_key_args()


    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    select_pod_policy(modir, frabic_policy_group)

    modir.logout()


