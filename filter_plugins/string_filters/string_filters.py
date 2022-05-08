# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause


def string_count(s, sub):
    return str(s).count(sub)


def string_find(s, sub):
    return str(s).find(sub)


def string_prefix(s, prefix):
    return prefix + str(s)


def string_postfix(s, postfix):
    return str(s) + postfix


def string_replace(s, old, new, *i):
    if len(i) == 0:
        return str(s).replace(old, new)
    else:
        return str(s).replace(old, new, i[0])


def string_split(s, *i):
    if len(i) == 0:
        return str(s).split()
    elif len(i) == 1:
        return str(s).split(i[0])
    else:
        return str(s).split(i[0], i[1])


class FilterModule(object):
    ''' Ansible filters. Interface to Python string methods.
        https://docs.python.org/3/library/stdtypes.html#string-methods
    '''

    def filters(self):
        return {
            'string_count': string_count,
            'string_find': string_find,
            'string_prefix': string_prefix,
            'string_postfix': string_postfix,
            'string_replace': string_replace,
            'string_split': string_split,
        }
