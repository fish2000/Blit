#!/usr/bin/env python
# encoding: utf-8

import os
from distutils.core import setup

# PROJECT DIRECTORY
PROJECT_NAME = 'Blit'
CWD = os.path.dirname(__file__)
BASE_PATH = os.path.join(
            os.path.abspath(CWD), PROJECT_NAME)

__version__ = "<undefined>"
try:
    exec(compile(
        open(os.path.join(BASE_PATH,
            '__version__.py')).read(),
            '__version__.py', 'exec'))
except:
    __version__ = '1.4.0'

setup(name=PROJECT_NAME,
      version=__version__,
      description='Simple pixel-composition library.',
      author='Michal Migurski',
      author_email='mike@stamen.com',
      url='https://github.com/migurski/Blit',
      requires=['numpy', 'sympy', 'Pillow'],
      packages=['Blit'],
      scripts=[],
      data_files=[],
      download_url='https://github.com/downloads/fish2000/Blit/Blit-%(__version__)s.tar.gz' % locals(),
      license='BSD')
