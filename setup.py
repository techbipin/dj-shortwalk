#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from setuptools import setup, find_packages

# Check if setuptools is installed and upgrade if necessary
try:
    import setuptools
except ImportError:
    print("setuptools is not installed. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])

# Function to check if a package is already installed
def is_package_installed(package_name):
    try:
        import pkg_resources
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

# Define the package name
package_name = "dj-shortwalk"

# Check if the package is already installed
if is_package_installed(package_name):
    print(f"The package '{package_name}' is already installed.")
    sys.exit(0)

# Read the content of the README file for long description
readme = ''
try:
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
except FileNotFoundError:
    print("Warning: README.rst not found. Skipping long description.")

version = '1.0'

# Run the setup function to install the package
setup(
    name='dj-shortwalk',
    version=version,
    description="For irritated Django developers who type 'python manage.py' too many times...",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author="Mr. Bipin Rajesh Tatkare",
    author_email="techbipinrt2526@gmail.com",
    url="https://github.com/techbipin/dj-shortwalk",
    packages=find_packages(where="dj_shortwalk"),
    py_modules=['dj_shortwalk'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'dj-shortwalk = dj_shortwalk.dj_shortwalk.main',
        ],
    },
    python_requires='>=3.12',
)