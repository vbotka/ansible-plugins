# All rights reserved (c) 2022-2023, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pandas as pd


def pandas_json_normalize(d):
    df = pd.json_normalize(d)
    l_temp = [df.columns.values.tolist()] + df.values.tolist()
    return(l_temp)


def pandas_duplicated(d, subset=None, keep='first', idx=False):
    df = pd.DataFrame(d)
    d_temp = df.duplicated(subset=subset, keep=keep).to_dict()
    if idx:
        return([k for k, v in d_temp.items() if v])
    else:
        return(d_temp)


def pandas_idx_duplicated(l, keep='first'):
    idx = pd.Index(l)
    l_temp = idx.duplicated(keep=keep).tolist()
    return(l_temp)


def pandas_drop_duplicates(d, subset=None, keep='first', inplace=True, ignore_index=False):
    df = pd.DataFrame(d)
    df.drop_duplicates(subset=subset, keep=keep, inplace=inplace, ignore_index=ignore_index)
    d_temp = df.to_dict('records')
    return(d_temp)


class FilterModule(object):
    ''' Ansible filters. Interface to https://pandas.pydata.org/. '''

    def filters(self):
        return {
            'pandas_json_normalize': pandas_json_normalize,
            'pandas_duplicated': pandas_duplicated,
            'pandas_idx_duplicated': pandas_idx_duplicated,
            'pandas_drop_duplicates': pandas_drop_duplicates,
        }
