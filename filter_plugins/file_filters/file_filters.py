# All rights reserved (c) 2019, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import mmap

def file_list_search(list, string):
    for file in list:
        if file_search(file, string):
            break
    return file_search(file, string)

def file_search(file, string):
    f = open(file)
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(string) != -1:
        return True
    else:
        return False

class FilterModule(object):
    ''' Ansible filters for operating on files '''

    def filters(self):
        return {
            'file_search' : file_search,
            'file_list_search' : file_list_search
        }
