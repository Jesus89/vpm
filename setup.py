#!/usr/bin/env python

from setuptools import setup

import imp
voh = imp.load_source('voh', './voh')

setup(name='voh',
      version=voh.__version__,
      description=voh.__doc__,
      author=voh.__author__,
      author_email=voh.__email__,
      url='https://github.com/Jesus89/voh',
      download_url='https://pypi.python.org/pypi/voh',
      license=voh.__license__,
      scripts=['voh'],
      install_requires=['gitpython==1.0.1'],
      classifiers=['Development Status :: 1 - Planning',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4'])
