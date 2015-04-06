#!/usr/bin/env python

__author__ = 'noisufnoc'

import os
import sys
import tarfile
from ConfigParser import SafeConfigParser

# Read in config file
# TODO: If I want to get crazy, let user provide config path other than default

CONFIG = 'splunkENV.ini'

if os.path.isfile(CONFIG):
    parser = SafeConfigParser()
    parser.read('splunkENV.ini')

    USER = parser.get('user', 'username')
    PASSWORD = parser.get('user', 'password')

    LIC = parser.get('env', 'license')
    DIR = parser.get('env', 'install_dir')
    SPLUNK = parser.get('env', 'splunk')
else:
    print 'You don\'t have any config'
    sys.exit(1)

# TODO: untar splunk as root into install_dir/env_name
# TODO: set env_name if not set before
# TODO: start and accept license
# TODO: handle ports in use
# TODO: add user/password
# TODO: add user as admin role
# TODO: add license
# TODO: restart splunk

def install(env_name):
    # install it here
