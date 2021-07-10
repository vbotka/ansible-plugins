# All rights reserved (c) 2021, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.module_utils.six import string_types
from ansible.module_utils.common._collections_compat import Mapping, Sequence

from pandas.io.json import json_normalize

def pandas_json_normalize(d):
    df = json_normalize(d)
    l = [df.columns.values.tolist()] + df.values.tolist()
    return(l)


class FilterModule(object):
    ''' Ansible filters. Interface to https://pandas.pydata.org/.'''

    def filters(self):
        return {
            'pandas_json_normalize': pandas_json_normalize,
        }
