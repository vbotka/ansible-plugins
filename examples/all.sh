#!/bin/sh

#export ANSIBLE_STDOUT_CALLBACK=default
export ANSIBLE_STDOUT_CALLBACK=actionable
#export ANSIBLE_STDOUT_CALLBACK=stderr

ansible-playbook bool_utils.yml
ansible-playbook dict_utils.yml
ansible-playbook hash_utils.yml
ansible-playbook list_methods.yml
ansible-playbook sort_versions.yml
ansible-playbook string_filters.yml
