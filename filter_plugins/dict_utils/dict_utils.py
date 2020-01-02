# All rights reserved (c) 2019, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import sys
import json

def list_flatten(l):
    flat_list = []
    for sublist in l:
        if isinstance(sublist, (list,)):
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    l = flat_list
    return l

def dict_merge(x, y):
    d = x.copy()
    d.update(y)
    return d

def dict_merge_lossless(x, y):
    d = x.copy()
    d.update(y)
    for key, value in d.items():
       if key in x and key in y:
               d[key] = [value , x[key]]
    return d

def dict_add_hash(d, h, recursive=False):
    if recursive:
        for k, v in h.iteritems():
            d[k] = [d[k],v]
    else:
        for k, v in h.iteritems():
            d[k] = v
    if isinstance(d[k], (list,)):
        d[k] = list_flatten(d[k])
    return d

def dict_del_key(d, key):
    del d[key]
    return d

def dict_keys(d):
    return list(d)

def dict_sorted(d):
    return sorted(d)

def dict_search_key(d, key):
    return key in d

def dict_prefix_keys(d, prefix='prefix_'):
    for key in d.keys():
        d[prefix + key] = d.pop(key)
    return d

def dict_flatten(d, separator='.'):
    ''' Credit: Flattening JSON objects in Python by Amir Ziai
        https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10'''

    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + separator)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + separator)
                i += 1
        else:
            out[name[:-1]] = x

    flatten(d)
    return out

def dict_sortbysubkey(d, k):
    return sorted(d.items(), key=lambda x: x[1][k])

def dict2list(d):
    l = []
    for i in d:
        h = {i:d[i]}
        l.append(h)
    return l

def item2dict(t):
    h = {t[0]:t[1]}
    return h

class FilterModule(object):
    ''' Ansible filters. Interface to Python dictionary methods.

        5.5. Dictionaries
        https://docs.python.org/3/tutorial/datastructures.html#dictionaries'''

    def filters(self):
        return {
            'dict_add_hash' : dict_add_hash,
            'dict_del_key' : dict_del_key,
            'dict_keys' : dict_keys,
            'dict_merge' : dict_merge,
            'dict_merge_lossless' : dict_merge_lossless,
            'dict_sorted' : dict_sorted,
            'dict_search_key' : dict_search_key,
            'dict_prefix_keys' : dict_prefix_keys,
            'dict_flatten': dict_flatten,
            'dict_sortbysubkey': dict_sortbysubkey,
            'dict2list': dict2list,
            'item2dict': item2dict
        }
