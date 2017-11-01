#!/bin/sh
if [ -f requirements.yml ]; then
  ansible-galaxy install -vvv -r requirements.yml
fi
