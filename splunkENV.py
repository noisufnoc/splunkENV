#!/usr/bin/env python

# do stuff

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('splunkENV.ini')

print parser.get('user', 'username')
print parser.get('env', 'splunk_home')

# TODO: untar splunk as root into install_dir/env_name
# TODO: set env_name if not set before
# TODO: start and accept license
# TODO: handle ports in use
# TODO: add user/password
# TODO: add user as admin role
# TODO: add license
# TODO: restart splunk
