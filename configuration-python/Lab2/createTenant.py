from utility import *


def create_tenant(modir, tenant_name):
    """Create a tenant"""
    policy_universe = modir.lookupByDn('uni')
    fvTenant = Tenant(policy_universe, tenant_name)

    # print the query in XML format
    print_query_xml(policy_universe)

    # Commit the change using a ConfigRequest object
    commit_change(modir, policy_universe)


if __name__ == '__main__':
    if len(sys.argv) == 5:
        host_name, user_name, password, tenant_name = sys.argv[1:]
    else:
        try:
            data = read_config_yaml_file(sys.argv[1])
            host_name = data['host_name']
            user_name = data['user_name']
            password = data['password']
            tenant_name = data['tenant_name']
        except (IOError, KeyError, TypeError):
            host_name, user_name, password = input_login_info()
            tenant_name = input_tenant_name()

    modir = apic_login(host_name, user_name, password)
    create_tenant(modir, tenant_name)
    modir.logout()
