# All rights reserved (c) 2020, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

def contains(list, value):
    """Test value is in the list"""
    return value in list


class TestModule:
    ''' Ansible list jinja2 tests '''

    def tests(self):
        return {
            'contains': contains,
        }
