#!/bin/sh

#export ANSIBLE_STDOUT_CALLBACK=default
export ANSIBLE_STDOUT_CALLBACK=actionable
#export ANSIBLE_STDOUT_CALLBACK=stderr

# Filter plugins
ansible-playbook acme_filters.yml
ansible-playbook bool_filters.yml
ansible-playbook dict_filters.yml
ansible-playbook hash_filters.yml
ansible-playbook list_filters.yml
ansible-playbook version_filters.yml
ansible-playbook string_filters.yml
ansible-playbook file_filters.yml
ansible-playbook datetime_filters.yml

# Inventory plugins
ANSIBLE_CONFIG=$PWD/ansible-inventory-ip_based_groups.cfg ansible-playbook inventory-ip_based_groups.yml
