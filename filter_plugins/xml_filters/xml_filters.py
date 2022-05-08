# All rights reserved (c) 2019-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

import json
import xmltodict


def xml_to_json(xml_data):
    """ Convert XML data to JSON """
    return json.dumps(xmltodict.parse(xml_data))


class FilterModule(object):
    ''' Ansible filters for xml '''

    def filters(self):
        return {
            'xml_to_json': xml_to_json,
        }
