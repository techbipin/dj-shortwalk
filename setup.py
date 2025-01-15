#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
import pkg_resources

# Make sure setuptools is installed. If not, try to install it automatically
try:
    import setuptools
except ImportError:
    print("setuptools is not installed. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])

# Function to check if a package is already installed
def is_package_installed(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

# Define the package name to be installed
package_name = "dj-shortwalk"

# Check if the package is already installed
if is_package_installed(package_name):
    print(f"The package '{package_name}' is already installed.")
    
    # Exit the script if the package is already installed to avoid reinstalling
    sys.exit(0)

# Import setup function to continue with the package installation
from setuptools import setup

# Read the content of the README file for long description
readme = open('README.rst').read()

# Run the setup function to install the package
setup(
    name='dj-shortwalk',
    version='1.0',
    description="For Irritated Django developers who types 'python manage.py' too many times...",
    long_description=readme,
    author="Mr. Bipin Rajesh Tatkare",
    author_email="techbipinrt2526@gmail.com",
    url="http://github.com/techbipin/dj-shortwalk",
    py_modules=['dj_shortwalk'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12'
    ],
    entry_points={
        'console_scripts': [
            'dj = dj_shortwalk:main',
        ]
    },
)
