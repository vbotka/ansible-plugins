# All rights reserved (c) 2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from pandas.io.json import json_normalize


def pandas_json_normalize(d):
    df = json_normalize(d)
    l_temp = [df.columns.values.tolist()] + df.values.tolist()
    return(l_temp)


class FilterModule(object):
    ''' Ansible filters. Interface to https://pandas.pydata.org/. '''

    def filters(self):
        return {
            'pandas_json_normalize': pandas_json_normalize,
        }
