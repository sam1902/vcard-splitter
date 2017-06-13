#!/usr/bin/python

from setuptools import setup

setup(name='vcard-splitter',
      version='0.1',
      description='A simple vCard splitter',
      url='https://github.com/sam1902/vcard-splitter',
      author='Samuel Prevost',
      author_email='s@muel.coffee',
      license='MIT',
      packages=['vcard-splitter'],
      zip_safe=False,
      long_description='A simple vCard splitter that, from one big vCard file containing multiple contact, create multiple vCard files (one for each contact) in the desired output directory with the desired name format.')