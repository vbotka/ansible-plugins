#
# Copyright 2019 Vladimir Botka <vbotka@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

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
 
def list_sort(l, my_key=None, my_reverse=False):
    l.sort(key=my_key, reverse=my_reverse)
    return l

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

class FilterModule(object):
    ''' Ansible filters. Interface to Python list methods.

        5.1. More on Lists
        https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        Methods of list objects.'''


    def filters(self):
        return {
            'list_append' : list_append,
            'list_clear' : list_clear,
            'list_copy' : list_copy,
            'list_count' : list_count,
            'list_extend' : list_extend,
            'list_flatten' : list_flatten,
            'list_index' : list_index,
            'list_insert' : list_insert,
            'list_pop' : list_pop,
            'list_remove' : list_remove,
            'list_reverse' : list_reverse,
            'list_search' : list_search,
            'list_sort' : list_sort,
            'list_sample' : list_sample
        }
