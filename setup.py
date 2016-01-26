#!/usr/bin/env python

from setuptools import setup

import vpm

setup(name='vpm',
      version=vpm.__version__,
      description=vpm.__doc__,
      author=vpm.__author__,
      author_email=vpm.__email__,
      url='https://github.com/Jesus89/vpm',
      download_url='https://pypi.python.org/pypi/vpm',
      license=vpm.__license__,
      py_modules=['vpm'],
      entry_points={'console_scripts': ['vpm=vpm:main']},
      install_requires=['gitpython==1.0.1'],
      classifiers=['Development Status :: 1 - Planning',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4'])
