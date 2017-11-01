#!/bin/sh
if [ -f requirements.yml ]; then
  sudo ansible-galaxy install -vvv -r requirements.yml
fi
