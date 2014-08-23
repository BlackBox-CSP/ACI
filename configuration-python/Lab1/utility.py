import sys
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant

from cobra.internal.codec.xmlcodec import toXMLStr


def apic_login(hostname, username, password):
    """Login to APIC"""
    lsess = LoginSession('https://'+hostname, username, password)
    modir = MoDirectory(lsess)
    modir.login()
    return modir


def check_if_tenant_exist(modir, tenant_name):
    fv_tenant = modir.lookupByDn('uni/tn-' + tenant_name)
    if not isinstance(fv_tenant, Tenant):
        print 'Tenant', tenant_name, 'does not existed. \nPlease create a tenant.'
        sys.exit()
    return fv_tenant


def get_raw_input(prompt='', lower=False, required=False):
    r_input = raw_input(prompt).strip()
    if required and r_input == '':
        return get_raw_input(prompt, lower=lower, required=required)
    return r_input.lower() if lower else r_input


def get_optional_input(prompt, options, num_accept=False, required=False):
    try:
        opt_string = '/'.join(options)
    except NameError:
        opt_string = ''
    opt_string = '[' + opt_string + ']: ' if not opt_string == '' else ': '
    r_input = get_raw_input(prompt + opt_string)
    if r_input == '':
        if required:
            return get_optional_input(prompt, options, num_accept=num_accept, required=required)
        else:
            return r_input

    opt = [a for a in options if a.startswith(r_input)]
    if len(opt) > 0:
        opt = opt[0].split('(')
        opt = opt[0]
        return opt
    elif num_accept:
        try:
            return int(r_input)
        except ValueError:
            pass
    print 'Not appropriate argument, please try again.'
    get_optional_input(prompt, options, num_accept=num_accept, required=required)


def get_yes_no(prompt='', required=False):
    r_input = raw_input(prompt+' [yes(y)/no(n)]?: ')
    if required and r_input == '':
        return get_yes_no(prompt=prompt, required=required)
    if r_input.lower() in ['yes', 'y', 'true']:
        return True
    elif r_input.lower() in ['no', 'n', 'false'] or r_input == '':
        return False
    else:
        print 'Inappropriate input.'
        get_yes_no(prompt=prompt, required=required)


def input_login_info(msg='\nPlease follow the wizard and finish the configuration.'):
    print msg
    print 'Login info:'
    return [get_raw_input("Host Name (required): ", required=True),
            get_raw_input("User Name (required): ", required=True),
            get_raw_input("Password (required): ", required=True)]


def input_tenant_name(msg='\nPlease input Tenant info:'):
    print msg
    return get_raw_input("Tenant Name (required): ", required=True)


def input_application_name(msg='\nPlease input Application info:'):
    print msg
    return get_raw_input("Application Name (required): ", required=True)


def commit_change(modir, changed_object):
    """Commit the changes to APIC"""
    config_req = ConfigRequest()
    config_req.addMo(changed_object)
    modir.commit(config_req)


def get_value(args, key, default_value):
    """Return the value of an argument. If no such an argument, return a default value"""
    return args[key] if key in args.keys() and args[key] != '' else default_value


def print_query_xml(xml_file, pretty_print=True):
    print toXMLStr(xml_file, prettyPrint=pretty_print)


# add a list the the same type MOs that only have key arguments
def add_mos(function, msg):
    mos = []
    add_one_mo = get_yes_no(prompt=msg, required=True)
    msg = msg.replace(' a ', ' another ')
    while add_one_mo:
        mos.append(function())
        add_one_mo = get_yes_no(prompt=msg, required=True)
    return mos


# add a list the the same type MOs that with optional arguments
def add_mos_with_options(key_function, opt_args_function, msg):
    mos = []
    add_one_mo = get_yes_no(prompt=msg, required=True)
    msg = msg.replace(' a ', ' another ')
    while add_one_mo:
        new_mo = []
        new_mo.append(key_function())
        new_mo.append(opt_args_function(new_mo[0]))
        mos.append(new_mo)
        add_one_mo = get_yes_no(prompt=msg, required=True)
    return mos