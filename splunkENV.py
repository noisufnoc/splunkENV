#!/usr/bin/env python

# do stuff

import os
import sys
from ConfigParser import SafeConfigParser

# Read in config file
# TODO: Check file exists

CONFIG = 'splunkENV.ini'

if os.path.isfile(CONFIG):
    parser = SafeConfigParser()
    parser.read('splunkENV.ini')
else:
    print 'You don\'t have any config'
    sys.exit(1)

print parser.get('user', 'username')
print parser.get('env', 'install_dir')

# TODO: untar splunk as root into install_dir/env_name
# TODO: set env_name if not set before
# TODO: start and accept license
# TODO: handle ports in use
# TODO: add user/password
# TODO: add user as admin role
# TODO: add license
# TODO: restart splunk
