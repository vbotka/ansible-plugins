# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types
from ansible.module_utils.common._collections_compat import Mapping, Sequence
from collections import defaultdict
from operator import itemgetter
import re
import random


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
    return sorted(l, key=ls_key, reverse=ls_reverse)


def list_sort_list(l, index, ls_reverse=False):
    return sorted(l, key=itemgetter(index), reverse=ls_reverse)


def list_sort_dict(l, attr, ls_reverse=False):
    return sorted(l, key=lambda i: i[attr], reverse=ls_reverse)


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
    return flat_list


def list_sample(l, n):
    return random.sample(l, n)


def list_zip(l, k):
    return zip(l, k)


def list_dict_zip(l, k):
    return dict((x, y) for x, y in zip(l, k))


def list_dict_zip_rev(l, k):
    return dict((y, x) for x, y in zip(l, k))


def list_list2dict(l):
    out = []
    for i in l:
        item = {}
        for j in range(0, len(i)):
            item.update(i[j])
        out.append(item)
    return out


def list_split_period(l, p):
    split_list = []
    j = p
    for i in range(p, len(l) + p, p):
        if i == p:
            split_list.append(l[0:p])
        elif i > len(l):
            split_list.append(l[j:])
        else:
            split_list.append(l[j:i])
        j = i
    return split_list


def list_select_list_bool(b, l, negative=False):
    l2 = []
    for bi, li in zip(b, l):
        if negative:
            if not bi:
                l2.append(li)
        else:
            if bi:
                l2.append(li)
    return l2


def list_range(l):
    return [i for i in range(*l)]


# def list_wrapper(l, func):
#     return func(*l)

# def list_wrapper_comp(l, func):
#     return [i for i in func(*l)]

# Upstream: community.general
def lists_mergeby(l1, l2, index):
    ''' merge lists by attribute index. Example:
        - debug: msg="{{ l1|lists_mergeby(l2, 'index')|list }}" '''

    if not isinstance(l1, Sequence):
        raise AnsibleFilterError('First argument for lists_mergeby must be list. %s is %s' %
                                 (l1, type(l1)))

    if not isinstance(l2, Sequence):
        raise AnsibleFilterError('Second argument for lists_mergeby must be list. %s is %s' %
                                 (l2, type(l2)))

    if not isinstance(index, string_types):
        raise AnsibleFilterError('Third argument for lists_mergeby must be string. %s is %s' %
                                 (index, type(index)))

    d = defaultdict(dict)
    for l in (l1, l2):
        for elem in l:
            if not isinstance(elem, Mapping):
                raise AnsibleFilterError('Elements of list arguments for lists_mergeby must be dictionaries. Found {0!r}.'.format(elem))
            if index in elem.keys():
                d[elem[index]].update(elem)
    return sorted(d.values(), key=itemgetter(index))


def any2items(x, key='key', override=False):
    ''' Convert any input to list.

    Example 1:

    - name: No changes to a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: [apple, banana, orange]

       gives:

       msg:
         - apple
         - banana
         - orang

    Example 2:

    - name: Convert string to first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: 'apple'

       gives:

       msg:
         - apple

    Example 3:

    - name: Convert None to first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: None

       gives:

       msg:
         - None

    Example 4:

    - name: Convert dictionary where all values are dictionaries to a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small

       gives:

       msg:
         - color: green
           key: apple
           size: big
         - color: yellow
           key: banana
           size: small

    Example 5:

    - name: Same as the above but change key name
      debug:
        msg: "{{ fruits|any2items(key='name') }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small

       gives:

       msg:
         - color: green
           name: apple
           size: big
         - color: yellow
           name: banana
           size: small

    Example 6:

    - name: Convert dictionary where NOT all values are dictionaries
            to a first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small
          orange: ripe

       gives:

       msg:
         - apple:
             color: green
             size: big
           banana:
             color: yellow
             size: small
           orange: ripe

    Example 7:

    - name: Convert dictionary where NOT all values are dictionaries
            to a first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple: green
          banana: yellow
          orange: ripe

       gives:

       msg:
         - apple: green
           banana: yellow
           orange: ripe

    Example 8:

    - name: Iterate any data by any2items
      debug:
        var: item
      loop: "{{ [{'a': 1},{'b': 2}]|any2items }}"

    - name: Iterate any data by any2items
      debug:
        var: item
      loop: "{{ {'c': 3}|any2items }}"

    '''

    if not isinstance(key, string_types):
        raise AnsibleFilterError('Argument key for any2items must be string. %s is %s' %
                                 (key, type(key)))
    if not isinstance(override, bool):
        raise AnsibleFilterError('Argument override for any2items must be boollean. %s is %s' %
                                 (override, type(override)))

    if isinstance(x, Mapping):
        keys = list(x.keys())
        values = list(x.values())
        if all(isinstance(value, Mapping) for value in values):
            if (not override) and any(key in list(value.keys()) for value in values):
                raise AnsibleFilterError('Key %s present in the dictionary.' % (key))
            else:
                l_temp = values
                for idx, item in enumerate(values):
                    z = item.copy()
                    z.update({key: keys[idx]})
                    l_temp[idx] = z
        else:
            l_temp = []
            l_temp.insert(0, x)
        return l_temp
    elif isinstance(x, string_types):
        l_temp = []
        l_temp.insert(0, x)
        return l_temp
    elif isinstance(x, Sequence):
        l_temp = list(x)
        return l_temp
    else:
        l_temp = []
        l_temp.insert(0, x)
        return l_temp


def items2dict2(mylist, key_name='key', value_name='value', default_value=None):
    ''' takes a list of dicts with each having a 'key' and 'value' keys, and transforms the list into a dictionary,
        effectively as the reverse of dict2items. If 'value_name' does not exist use 'default_value'.  '''

    if not isinstance(mylist, Sequence):
        raise AnsibleFilterError("First argument for community.general.items2dict2 requires a list. %s is %s" %
                                 (mylist, type(mylist)))

    return dict((item[key_name], item.setdefault(value_name, default_value)) for item in mylist)


def list_test(l1, l2, index):
    d = defaultdict(dict)
    for l in (l1, l2):
        for elem in l:
            if index in elem.keys():
                d[elem[index]].update(elem)
    return sorted(d.values(), key=itemgetter(index))


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
            'list_list2dict': list_list2dict,
            'list_split_period': list_split_period,
            'list_select_list_bool': list_select_list_bool,
            'list_range': list_range,
            # 'list_wrapper': list_wrapper,
            # 'list_wrapper_comp': list_wrapper_comp,
            'lists_mergeby': lists_mergeby,
            'list_test': list_test,
            'any2items': any2items,
            'items2dict2': items2dict2,
        }
