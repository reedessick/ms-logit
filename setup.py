#!/usr/bin/env python
__usage__ = "setup.py command [--options]"
__description__ = "standard install script"
__author__ = "Reed Essick (essick@cita.utoronto.ca)"

#-------------------------------------------------

from setuptools import (setup, find_packages)
import glob

#-------------------------------------------------

# set up arguments
scripts = glob.glob('bin/*')

packages = find_packages()
package_data = {}

# set up requirements
requires = [
    'numpy',
    'numpyro',
]

#------------------------

# install
setup(
    name = 'ms_logit',
    version = '0.0.0',
    url = 'https://github.com/reedessick/ms-logit',
    author = __author__,
    author_email = 'essick@cita.utoronto.ca',
    description = __description__,
    license = 'MIT',
    scripts = scripts,
    packages = packages,
    package_data = package_data,
    install_requires = requires,
)
