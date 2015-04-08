#!/usr/bin/env python

__author__ = 'noisufnoc'

import os
import sys
import tarfile
from subprocess import call
from ConfigParser import SafeConfigParser

# Read in config file
# TODO: If I want to get crazy, let user provide config path other than default
# TODO: must be root, sorry

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

# TODO: handle ports in use


def install(env_name, source, destination):
    # install it here

    source_tar = tarfile.open(source)
    source_tar.extractall(destination)

    env_path = destination + '/' + env_name
    os.rename(destination + '/splunk', env_path)

    return True, env_path


def config(env_path, license, user, password, email, name, adminpass):
    # config/start it here
    splunk_bin = env_path + '/bin/splunk'
    call([splunk_bin, 'start', '--accept-license'])
    # set admin password
    call([splunk_bin, 'edit', 'user', 'admin', '-password', adminpass,
          '-roles', 'admin', '-auth', 'admin:changeme'])
    call([splunk_bin, 'add', 'license', license,
          '-auth', 'admin:%s' % adminpass])
    call([splunk_bin, 'add', 'user', user, '-password',
          password, '-role', 'admin', '-email', email,
          '-realname', name, '-auth', 'admin:%s' % adminpass])
    call([splunk_bin, 'restart'])


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
