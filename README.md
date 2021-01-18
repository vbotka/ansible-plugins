# Ansible plugins

Various Ansbile plugins.


## Installation

- Use Ansible Galaxy Role [ansible](https://galaxy.ansible.com/vbotka/ansible) to install selected plugins
- See [examples in role vars](https://github.com/vbotka/ansible-ansible/blob/master/vars/main.yml.sample)
- See [examples in docs](https://ansible-ansible.readthedocs.io/en/latest/guide.html#examples)


## Filter plugins

- **acme_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/acme_filters.yml)
- **bool_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/bool_filters.yml)
- **datetime_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/datetime_filters.yml)
- **dict_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/dict_filters.yml)
- **file_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/file_filters.yml)
- **hash_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/hash_filters.yml)
- **list_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/list_filters.yml)
- **netaddr_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/netaddr_filters.yml)
- **string_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/string_filters.yml)
- **version_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/version_filters.yml)
- **xml_filters** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/xml_filters.yml)


## Test plugins

- **list_tests** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/list_tests.yml)


## Inventory plugins

- **ip_based_groups** see [examples](https://github.com/vbotka/ansible-plugins/blob/master/examples/inventory-ip_based_groups.sh)


## References

- [Working With Plugins](https://docs.ansible.com/ansible/latest/plugins/plugins.html#working-with-plugins)
- [acme - ACME: Automatic Certificate Management Environment RFC 8555](https://tools.ietf.org/html/rfc8555)
- [acme - Letsencrypt: Certificate Authority providing TLS certificates](https://letsencrypt.org/)
- [acme - Certbot: Software tool for automatically using Lets Encrypt certificates](https://certbot.eff.org/)
- [acme - ASN1: Abstract Syntax Notation One](https://www.oss.com/asn1/resources/standards-define-asn1.html)
- [acme - DER vs. CRT vs. CER vs. PEM Certificates and How To Convert Them](https://support.ssl.com/Knowledgebase/Article/View/19/0/der-vs-crt-vs-cer-vs-pem-certificates-and-how-to-convert-them)
- [acme - pyOpenSSL: Wrapper around (a subset of) the OpenSSL library](https://www.pyopenssl.org/en/stable/)
- [acme - cryptography: Interfaces to common cryptographic algorithms in Python](https://cryptography.io/en/latest/)
- [bool - Built-in Functions](https://docs.python.org/3/library/functions.html)
- [datetime - Basic date and time types](https://docs.python.org/3/library/datetime.html)
- [dict - Rename a dictionary key](https://stackoverflow.com/questions/16475384/rename-a-dictionary-key)
- [dict - 5.5. Dictionaries docs.python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [file - How to search for a string in text files?](https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files)
- [hash - Iterating a hash in an Ansible task](https://coderwall.com/p/rxsmvw/iterating-a-hash-in-an-ansible-task)
- [list - More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [list - Sorting HOW TO](https://docs.python.org/3/howto/sorting.html#sortinghowto)
- [list - Ways to sort list of dictionaries by values in Python – Using lambda function](https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/)
- [netaddr - A network address manipulation library for Python](https://pypi.org/project/netaddr/)
- [netaddr - Python Network Programming](https://0xbharath.github.io/python-network-programming/index.html)
- [sort - How to sort complex version numbers in Ansible](https://stackoverflow.com/questions/56063612/how-to-sort-complex-version-numbers-in-ansible/)
- [string - String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)


## License

[![license](https://img.shields.io/badge/license-BSD-red.svg)](https://www.freebsd.org/doc/en/articles/bsdl-gpl/article.html)


## Author Information

[Vladimir Botka](https://botka.link)
