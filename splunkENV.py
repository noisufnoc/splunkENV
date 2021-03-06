#!/usr/bin/env python

__author__ = 'noisufnoc'

import os
import sys
import tarfile
from subprocess import call
from ConfigParser import SafeConfigParser

# Read in config file
# TODO: If I want to get crazy, let user provide config path other than default
# TODO: handle ports in use
# TODO: misc error checking
# TODO: handle dupe directories
# TODO: upgrade splunk versions
# TODO: update lic file
# TODO: take args to add new functions
# TODO: args: install, upgrade, lic, start, stop, status

CONFIG = 'splunkENV.ini'

if os.path.isfile(CONFIG):
    parser = SafeConfigParser()
    parser.read('splunkENV.ini')

    USER = parser.get('user', 'username')
    PASSWORD = parser.get('user', 'password')
    EMAIL = parser.get('user', 'email')
    NAME = parser.get('user', 'name')

    LIC = parser.get('env', 'license')
    DIR = parser.get('env', 'install_dir')
    SPLUNK = parser.get('env', 'splunk')
    ADMINPASS = parser.get('env', 'adminpass')
else:
    print 'You don\'t have any config'
    sys.exit(1)


def install(env_name, source, destination):
    # install it here

    source_tar = tarfile.open(source)
    source_tar.extractall(destination)

    env_path = destination + '/' + env_name
    os.rename(destination + '/splunk', env_path)
    # os.rename(destination + '/splunkbeta', env_path)

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
    call(['touch', '%s/etc/.ui_login' % env_path])
    call([splunk_bin, 'restart'])


def postinstall(env_path):
    # finish it here
    os.chdir(env_path)
    return True


def main():
    if not os.geteuid() == 0:
        # gotta be root, sorry.
        sys.exit('\nYou must be root to continue\n')
    if len(sys.argv) == 1:
        # No args, you suck
        sys.exit('\nYou must name your env, son.\n')
    else:
        env_name = sys.argv[1]

    status, env_path = install(env_name, SPLUNK, DIR)
    if not status:
        sys.exit('\nOH NO! Something bad happened\n')

    config(env_path, LIC, USER, PASSWORD, EMAIL, NAME, ADMINPASS)

    postinstall(env_path)


if __name__ == '__main__':
    main()
