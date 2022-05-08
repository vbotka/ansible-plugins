# All rights reserved (c) 2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import netaddr
from netaddr import IPNetwork


def netaddr_item(net, i):
    return str(list(IPNetwork(net))[i])


def netaddr_list(net):
    return [str(ip) for ip in list(IPNetwork(net))]


def netaddr_iter_iprange(ip_start, ip_end):
    return [str(ip) for ip in netaddr.iter_iprange(ip_start, ip_end)]


class FilterModule(object):
    ''' Ansible filters. Interface to netaddr methods.
        https://pypi.org/project/netaddr/
    '''

    def filters(self):
        return {
            'netaddr_item': netaddr_item,
            'netaddr_list': netaddr_list,
            'netaddr_iter_iprange': netaddr_iter_iprange,
        }

# EOF
