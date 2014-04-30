#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(name='eight',
      version='0.1',
      description='8-Puzzle Solver',
      author='Yusuke Miyazaki',
      author_email='miyazaki.dev@gmail.com',
      packages=['eight'],
      scripts=['scripts/eightpuzzle'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 3 - Alpha'
      ])
