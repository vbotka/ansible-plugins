#!/bin/sh

#export ANSIBLE_STDOUT_CALLBACK=default
export ANSIBLE_STDOUT_CALLBACK=actionable
#export ANSIBLE_STDOUT_CALLBACK=stderr

# Filter plugins
ansible-playbook bool_utils.yml
ansible-playbook dict_utils.yml
ansible-playbook hash_utils.yml
ansible-playbook list_methods.yml
ansible-playbook version_filters.yml
ansible-playbook string_filters.yml
ansible-playbook file_filters.yml
ansible-playbook datetime_filters.yml

# Inventory plugins
ANSIBLE_CONFIG=$PWD/ansible-inventory-ip_based_groups.cfg ansible-playbook inventory-ip_based_groups.yml
