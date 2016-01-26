#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the VPM Project

"""
VPM is a Verilog package manager based on GitHub.
Usage:

 * vpm list

 * vpm clear

 * vpm install id
 * vpm install user/repo

"""

__author__ = 'Jesús Arroyo Torrens'
__email__ = 'jesus.arroyo@bq.com'
__license__ = 'GPLv2'
__version__ = '0.0.2'

import os
import re
import json
import argparse


def parse_arguments():
    description = 'Verilog package manager.'
    parser = argparse.ArgumentParser(description=description)

    # Add dependency parameters
    parser.add_argument('-l', '--list', action='store_true', default=False,
                        help='List all official packages')
    parser.add_argument('-c', '--clear', action='store_true', default=False,
                        help='Clear all installed packages')
    parser.add_argument('-i', '--install', metavar='pkg',
                        help='Install package: "id" or "user/repo"')

    # Parse the arguments
    args = parser.parse_args()
    return args


def list_packages():
    import urllib2
    list_url = 'https://raw.githubusercontent.com/Jesus89/vpm/master/vpm.json'
    try:
        # Download JSON list
        response = urllib2.urlopen(list_url)
        packages = json.loads(response.read())
        return packages

    except Exception as e:
        pout('Error: ' + str(e))


def print_list(packages):
    # Sort list
    names = []
    for item in packages:
        names += [item['name']]
    names.sort()

    # Print list
    ret = 'Online packages:\n'
    for name in names:
        ret += ' * ' + name + '\n'
    pout(ret)


def clear_packages():
    import shutil
    # Remove vpm_modules dir
    path = os.path.join(os.getcwd(), "vpm_modules")
    pout('Remove installed packages')
    key = raw_input('Are you sure? [Y/N]: ')
    if key == 'y' or key == 'Y':
        if os.path.exists(path):
            shutil.rmtree(path)
        print('Done')
    else:
        print('Cancelled')


def pout(output=None):
    # Print header
    print('-------------------------')
    print(' Verilog package manager ')
    print('-------------------------')
    print('')
    if output is not None:
        print(output)


def install_package(package=None):
    if package is None:

        # Install dependencies from package.json
        pass

    elif _check_id_name(package):

        # Install package from id: name
        packages = list_packages()

        if _contains_package(package, packages):
            pout('Package "{0}" found'.format(package))

            # Download source
            source = _obtain_source(package, packages)
            _download_source(package, source)
        else:
            pout('Error: package "{0}" not found'.format(package))

    elif _check_id_user_repo(package):

        # Install package from id: user/repo
        source = 'https://github.com/' + package + '.git'
        pout()

        if _check_source(source):
            print('Package "{0}" found'.format(package))

            # Download source
            _download_source(package, source)
        else:
            print('Error: package "{0}" not found'.format(package))
    else:
        pout('Error: incorrect package')


def _check_id_name(package):
    return re.search(r'^[^\/]+$', package)


def _check_id_user_repo(package):
    return re.search(r'^[\w-]+\/[\w-]+$', package)


def _contains_package(package, packages):
    names = []
    for item in packages:
        names += [item['name']]
    return package in names


def _obtain_source(package, packages):
    source = None
    for item in packages:
        if package == item['name']:
            source = item['source']
            break
    return source


def _check_source(source):
    import urllib2
    try:
        # Check source
        urllib2.urlopen(source)
        return True
    except Exception:
        # print(str(e))
        return False


def _download_source(name, source):
    import git
    if _check_source(source):
        print('Downloading source...')

        # Create vpm_modules dir
        path = os.path.join(os.getcwd(), "vpm_modules")
        if not os.path.exists(path):
            os.makedirs(path)

        try:
            # Clone repository
            git.Repo.clone_from(source, os.path.join(path, name))
            print('Done')
        except git.exc.GitCommandError as e:
            print('Package already installed!')
        except Exception as e:
            print('Error :' + str(e))


def main():
    # Parse arguments
    args = parse_arguments()

    # List
    if args.list:
        print_list(list_packages())

    # Clear
    if args.clear:
        clear_packages()

    # Install packages
    if args.install:
        install_package(args.install)

    # Install dependencies
    if not args.list and not args.clear and not args.install:
        install_package()

if __name__ == '__main__':
    main()
