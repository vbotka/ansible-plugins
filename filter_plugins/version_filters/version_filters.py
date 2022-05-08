# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from distutils.version import LooseVersion


def version_sort(l):
    return sorted(l, key=LooseVersion)


def version_max(l):
    return sorted(l, key=LooseVersion)[-1]


def version_min(l):
    return sorted(l, key=LooseVersion)[0]


class FilterModule(object):
    ''' Ansible filters for operating on versions '''

    def filters(self):
        return {
            'version_sort': version_sort,
            'version_max': version_max,
            'version_min': version_min,
        }
