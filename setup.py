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
      url='https://github.com/litesystems/8puzzle',
      packages=['eight'],
      scripts=['scripts/eightpuzzle'],
      test_suite='tests',
      install_requires=[
          'matplotlib>=1.3.1',
          'networkx>=1.8.1',
          'pygraphviz>=1.2'
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7'
      ])
