#!/usr/bin/env python3
"""
Deploy application onto VM for appropriate environment if on an environment 
branch
"""

import os
import sys
from subprocess import check_call

EXIT_SUCCESS = 0

S_MASTER = 'master'
S_PRODUCTION = 'production'
S_STAGING = 'staging'
S_TEST = 'test'
S_TRAVIS_BRANCH = 'TRAVIS_BRANCH'
S_INVENTORY = 'inventory'
S_NO_REQUIRED_INVENTORY_ERROR_MSG = (
  'There is no {} file in the ansible-additions directory. This file is needed ' 
  'to deploy to the {} environment')
S_ANSIBLE_PLAYBOOK = 'ansible-playbook'
S_PLAYBOOK_YML = 'playbook.yml'
S_I_FLAG = '-i'
S_VVV_FLAG = '-vvv'
S_REQUIREMENTS_YML = 'requirements.yml'
S_ANSIBLE_GALAXY = 'ansible-galaxy'
S_INSTALL = 'install'
S_R_FLAG = '-r'

BRANCH_ENVIRONMENT_MAPPINGS = {
  S_MASTER: S_PRODUCTION,
  S_STAGING: S_STAGING,
  S_TEST: S_TEST
}

# If on an environment branch, translate the name of the branch to the 
# environment tag, otherwise, exit as feature branches will not be deployed
branch_name = os.environ[S_TRAVIS_BRANCH]
if branch_name not in BRANCH_ENVIRONMENT_MAPPINGS.keys():
    sys.exit(EXIT_SUCCESS)
env_tag = BRANCH_ENVIRONMENT_MAPPINGS[branch_name]

# Use Ansible to deloy to the correct VM
inventory_file_name = '{}-{}'.format(S_INVENTORY, env_tag)
# Make sure that required inventory file exists
if not os.path.isfile(inventory_file_name):
    exit(S_NO_REQUIRED_INVENTORY_ERROR_MSG.format(inventory_file_name, env_tag))
# Install Galaxy requirements if the file exists
if os.path.isfile(S_REQUIREMENTS_YML):
    check_call([S_ANSIBLE_GALAXY, S_INSTALL, S_R_FLAG, S_REQUIREMENTS_YML])
check_call([S_ANSIBLE_PLAYBOOK, S_PLAYBOOK_YML, S_I_FLAG, inventory_file_name,
      S_VVV_FLAG])
