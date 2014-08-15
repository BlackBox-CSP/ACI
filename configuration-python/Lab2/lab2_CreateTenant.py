import sys
from utility import *
from createTenant import create_tenant
from addSecurityDomain import add_security_domain
from addPrivateL3Network import add_private_l3_network
from addBridgeDomainSubnet import add_bridge_domain_subnet


def lab2(modir, tenant_name):
    """Following the Lab Guide, we create a tenant"""

    # Create a tenant. The tenant is defined by the user.
    create_tenant(modir, tenant_name)
    # Add two security domain
    add_security_domain(modir, tenant_name, 'all')
    add_security_domain(modir, tenant_name, 'mgmt')
    # Create private network
    private_l3_network = tenant_name+'_VRF'
    add_private_l3_network(modir, tenant_name, private_l3_network)
    # Create two bridge domains. Each one contains one subnet.
    add_bridge_domain_subnet(modir, tenant_name, tenant_name+'_BD1', '10.10.10.1/24', private_l3_network)
    add_bridge_domain_subnet(modir, tenant_name, tenant_name+'_BD2', '20.20.20.1/24', private_l3_network)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        hostname, username, password = input_login_info()
        tenant_name = input_tenant_name()
    else:
        hostname, username, password, tenant_name = sys.argv[1:]
    modir = apic_login(hostname, username, password)
    lab2(modir, tenant_name)
    modir.logout()
