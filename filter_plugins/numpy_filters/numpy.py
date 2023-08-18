# All rights reserved (c) 2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Sequence

import json
import numpy


def numpy_transpose(arr):
    if not isinstance(arr, Sequence):
        raise AnsibleFilterError('First argument for numpy_transpose must be list. %s is %s' %
                                 (arr, type(arr)))
    arr1 = numpy.array(arr)
    arr2 = arr1.transpose()
    return json.dumps(arr2.tolist())


def numpy_array_by_idx(arr, idx):
    if not isinstance(arr, Sequence):
        raise AnsibleFilterError('First argument for numpy_array_by_idx must be list. %s is %s' %
                                 (arr, type(arr)))
    if not isinstance(idx, Sequence):
        raise AnsibleFilterError('Second argument for numpy_array_by_idx must be list. %s is %s' %
                                 (idx, type(idx)))
    a = numpy.array(arr)
    return json.dumps(list(a[idx]))


class FilterModule(object):
    ''' Ansible wrappers for Python NumPy methods '''

    def filters(self):
        return {
            'numpy_transpose': numpy_transpose,
            'numpy_array_by_idx': numpy_array_by_idx,
        }
