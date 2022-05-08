# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause


def hash_to_tuple(h):
    return list(h.items())[0]


def hash_key(h):
    return list(h.keys())[0]


def hash_value(h):
    return list(h.values())[0]


def hash_to_tuples(h):
    return h.items()


def hash_keys(h):
    return h.keys()


def hash_values(h):
    return h.values()


class FilterModule(object):
    ''' Ansible filters for operating on hashes '''

    def filters(self):
        return {
            'hash_to_tuple': hash_to_tuple,
            'hash_key': hash_key,
            'hash_value': hash_value,
            'hash_to_tuples': hash_to_tuples,
            'hash_keys': hash_keys,
            'hash_values': hash_values,
        }
