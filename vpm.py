#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the VPM Project
#
#   Usage:
#
#   * npm install
#   * npm install id
#   * npm install user/repo
#
#   * npm list
#

"""
VPM is a Verilog package manager based on GitHub.
"""

__author__ = 'Jesús Arroyo Torrens'
__email__ = 'jesus.arroyo@bq.com'
__license__ = 'GPLv2'
__version__ = '0.0.1'


def parse_arguments():
    import argparse
    description = 'VPM. Verilog package manager.'
    parser = argparse.ArgumentParser(description=description)

    # Add dependency parameters
    parser.add_argument('-l', '--list', action='store_true', default=False,
                        help='List all official packages')
    parser.add_argument('-i', '--install', metavar='package',
                        help='Install package')

    # Parse the arguments
    args = parser.parse_args()

    return args


def list_packages():
    pass


def install_package(package):
    pass


def parse_json(filepath):
    import json

    # Load JSON file
    with open(filepath) as json_file:
        json_data = json.load(json_file)
        if 'dependencies' in json_data:
            for dep in json_data['dependencies']:
                user, repo = dep.split('/')
                print(user)
                print(repo)


def check_repository(user, repo):
    import urllib2
    try:
        # Try to connect to the repository
        urllib2.urlopen("https://github.com/" + user + "/" + repo)
        return True
    except urllib2.HTTPError as e:
        print("Error: " + str(e.code))
        return False
    except urllib2.URLError as e:
        print("Error: " + str(e.args))
        return False


def git_clone(user, repo):
    # Create vpm_modules dirg
    import os
    path = os.path.join(os.getcwd(), "vpm_modules")
    if not os.path.exists(path):
        os.makedirs(path)

    # Clone repository
    from git import Repo
    Repo.clone_from("https://github.com/" + user + "/" + repo + ".git",
                    os.path.join(path, repo))


if __name__ == '__main__':

    # Parse arguments
    args = parse_arguments()

    # List
    if args.list:
        list_packages()

    # Install
    if args.install:
        package = args.install
        install_package(package)
