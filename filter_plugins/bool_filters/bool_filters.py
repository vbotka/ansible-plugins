# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause


def bool_and(l):
    return all(l)


def bool_or(l):
    return any(l)


def bool_eq(a, b):
    return (a == b)


def bool_lt(a, b):
    return (a < b)


def bool_le(a, b):
    return (a <= b)


def bool_gt(a, b):
    return (a > b)


def bool_ge(a, b):
    return (a >= b)


def bool_ne(a, b):
    return (a != b)


def bool_is(a, b):
    return (a is b)


def bool_is_not(a, b):
    return (a is not b)


def bool_in(x, l):
    return (x in l)


def bool_in_not(x, l):
    return (x not in l)


class FilterModule(object):
    ''' Ansible filters for operating on Boolean '''

    def filters(self):
        return {
            'bool_and': bool_and,
            'bool_or': bool_or,
            'bool_eq': bool_eq,
            'bool_lt': bool_lt,
            'bool_le': bool_le,
            'bool_gt': bool_gt,
            'bool_ge': bool_ge,
            'bool_ne': bool_ne,
            'bool_is': bool_is,
            'bool_is_not': bool_is_not,
            'bool_in': bool_in,
            'bool_in_not': bool_in_not,
        }
