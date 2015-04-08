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


def install(env_name, license, source, destination):
    # install it here

    source_tar = tarfile.open(source)
    source_tar.extractall(destination)

    env_path = destination + '/' + env_name
    os.rename(destination + '/splunk', env_path)


def config(user, password):
    # config it here
    print 'foo'


def main():
    if len(sys.argv) == 1:
        # No args, you suck
        print 'You must name your env, son.'
        sys.exit(1)
    else:
        env_name = sys.argv[1]

    # do stuff, and then do more stuff
    install(env_name, LIC, SPLUNK, DIR)

if __name__ == '__main__':
    main()
