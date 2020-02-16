# All rights reserved (c) 2019-2020, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import re
import random
from operator import itemgetter, attrgetter

def list_append(l, x=''):
    l.append(x)
    return l

def list_extend(l, x=[]):
    l.extend(x)
    return l

def list_insert(l, i=0, x=''):
    l.insert(i, x)
    return l

def list_remove(l, x=''):
    l.remove(x)
    return l

def list_pop(l, *i):
    if len(i) == 0:
        return l.pop()
    else:
        return l.pop(i[0])

def list_clear(l):
    # l.clear()  # 'list' object has no attribute 'clear'
    del l[:]
    return l

def list_index(l, x, *i):
    if len(i) == 0:
        return l.index(x) if x in l else -1
    elif len(i) == 1:
        return l.index(x, i[0]) if x in l[i[0]:] else -1
    else:
        return l.index(x, i[0], i[1]) if x in l[i[0]:i[1]] else -1

def list_count(l, x):
    return l.count(x)
 
def list_sort(l, ls_key=None, ls_reverse=False):
    return sorted(l, key = ls_key, reverse = ls_reverse)

def list_sort_list(l, index, ls_reverse=False):
    return sorted(l, key = itemgetter(index), reverse = ls_reverse)

def list_sort_dict(l, attr, ls_reverse=False):
    return sorted(l, key = lambda i: i[attr], reverse = ls_reverse)

def list_reverse(l):
    l.reverse()
    return l

def list_copy(l):
    # l.copy()  # 'list' object has no attribute 'copy'
    return l[:]

def list_search(l, x):
    r = re.compile(x)
    return list(filter(r.match, l))

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

def list_sample(l,n):
    return random.sample(l,n)

def list_zip(l,k):
    return zip(l,k)

def list_dict_zip(l,k):
    return dict((x,y) for x,y in  zip(l,k))

def list_dict_zip_rev(l,k):
    return dict((y,x) for x,y in  zip(l,k))

def list_split_period(l, p):
    split_list = []
    for i in range(p, len(l)+p, p):
        if i == p:
            split_list.append(l[0:p])
        elif i > len(l):
            split_list.append(l[j:])
        else:
            split_list.append(l[j:i])
        j = i
    return split_list

def list_select_list_bool(b, l, negative=False):
    l2=[]
    for bi,li in zip(b,l):
        if negative:
            if not bi:
                l2.append(li)
        else:
            if bi:
                l2.append(li)
    return l2

class FilterModule(object):
    ''' Ansible filters. Interface to Python list methods.

        5.1. More on Lists
        https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        Methods of list objects.'''


    def filters(self):
        return {
            'list_append': list_append,
            'list_clear': list_clear,
            'list_copy': list_copy,
            'list_count': list_count,
            'list_extend': list_extend,
            'list_flatten': list_flatten,
            'list_index': list_index,
            'list_insert': list_insert,
            'list_pop': list_pop,
            'list_remove': list_remove,
            'list_reverse': list_reverse,
            'list_search': list_search,
            'list_sort': list_sort,
            'list_sort_list': list_sort_list,
            'list_sort_dict': list_sort_dict,
            'list_sample': list_sample,
            'list_zip': list_zip,
            'list_dict_zip': list_dict_zip,
            'list_dict_zip_rev': list_dict_zip_rev,
            'list_split_period': list_split_period,
            'list_select_list_bool': list_select_list_bool
        }
