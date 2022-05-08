#!/bin/sh

export ANSIBLE_STDOUT_CALLBACK=default
export ANSIBLE_DISPLAY_SKIPPED_HOSTS=no
export ANSIBLE_DISPLAY_OK_HOSTS=yes
#export ANSIBLE_STDOUT_CALLBACK=stderr

# Filter plugins
ansible-playbook acme_filters.yml
ansible-playbook bool_filters.yml
ansible-playbook datetime_filters.yml
ansible-playbook dict_filters.yml
ansible-playbook file_filters.yml
ansible-playbook hash_filters.yml
ansible-playbook list_filters.yml
ansible-playbook netaddr_filters.yml -e test_netaddr=true
ansible-playbook numpy_filters.yml -e test_numpy=true
ansible-playbook string_filters.yml
ansible-playbook pandas_filters.yml
ansible-playbook version_filters.yml
ansible-playbook xml_filters.yml

# Inventory plugins
ANSIBLE_CONFIG=$PWD/ansible-inventory-ip_based_groups.cfg ansible-playbook inventory-ip_based_groups.yml

# Test plugins
ansible-playbook list_tests.yml

# EOF
