#!/bin/sh

ANSIBLE_CONFIG=$PWD/ansible-inventory-ip_based_groups.cfg ansible-playbook inventory-ip_based_groups.yml
