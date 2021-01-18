# All rights reserved (c) 2021, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import netaddr

def netaddr_iter_iprange(ip_start, ip_end):
    return [str(ip) for ip in netaddr.iter_iprange(ip_start, ip_end)]

class FilterModule(object):
        ''' Ansible filters. Interface to netaddr methods.
            https://pypi.org/project/netaddr/
        '''

        def filters(self):
            return {
                'netaddr_iter_iprange' : netaddr_iter_iprange,
                }
