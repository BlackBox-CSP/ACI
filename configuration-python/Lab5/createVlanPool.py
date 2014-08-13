import sys
from cobra.mit.access import EndPoint, MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fvns import VlanInstP, EncapBlk

from cobra.internal.codec.xmlcodec import toXMLStr


def apic_login(hostname, username, password):
    """Login to APIC"""
    epoint = EndPoint(hostname, secure=False, port=80)
    lsess = LoginSession(username, password)
    modir = MoDirectory(epoint, lsess)
    modir.login()
    return modir


def commit_change(modir, changed_object):
    """Commit the changes to APIC"""
    config_req = ConfigRequest()
    config_req.addMo(changed_object)
    modir.commit(config_req)


def create_vlan_pool(modir, vlan_name, allocation_mode, vlan_range_from, vlan_range_to):

    # Query to the vlan pool collections.
    infra_infra = modir.lookupByDn('uni/infra')
    # Create a VLAN.
    fvns_vlaninstp = VlanInstP(infra_infra, vlan_name, allocation_mode)
    # Set up the VLAN range.
    fvns_encapblk = EncapBlk(fvns_vlaninstp, 'vlan-'+vlan_range_from, 'vlan-'+vlan_range_to)
    print toXMLStr(infra_infra, prettyPrint=True)
    commit_change(modir, infra_infra)

if __name__ == '__main__':

    # Obtain the key parameters.
    try:
        host_name, user_name, password, vlan_name, allocation_mode, vlan_range_from, vlan_range_to = sys.argv[1:8]
    except ValueError:
        print 'Usage:', __file__, '<hostname> <username> <password> <vlan_name> <allocation_mode> <vlan_range_from> <vlan_range_to>'
        sys.exit()

    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    if allocation_mode.lower() not in ['dynamic', 'static']:
        print 'VM provider has to be either be \"dynamic\" or \"static\"'
    else:
        create_vlan_pool(modir, vlan_name, allocation_mode.lower(), vlan_range_from, vlan_range_to)

    modir.logout()


