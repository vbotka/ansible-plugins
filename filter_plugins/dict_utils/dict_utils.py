# (c) 2019, Vladimir Botka <vbotka@gmail.com>
# All rights reserved.
# Simplified BSD License

# import list_methods

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
            'dict_sorted' : dict_sorted,
            'dict_search_key' : dict_search_key,
            'dict_prefix_keys' : dict_prefix_keys
        }
