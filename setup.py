#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup

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

def project_content(filename):
    import io
    filepath = os.path.join(CWD, filename)
    if not os.path.isfile(filepath):
        raise IOError("""File %s doesn't exist""" % filepath)
    out = ''
    with io.open(filepath, 'r') as handle:
        out += handle.read()
    if not out:
        raise ValueError("""File %s couldn't be read""" % filename)
    return out

LONG_DESCRIPTION = project_content('README.md')

setup(name=PROJECT_NAME,
      version=__version__,
      description='Simple pixel-composition library.',
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      author='Michal Migurski',
      author_email='mike@stamen.com',
      url='https://github.com/migurski/Blit',
      requires=['numpy', 'sympy', 'Pillow'],
      packages=['Blit'],
      scripts=[],
      data_files=[],
      download_url='https://github.com/downloads/fish2000/Blit/Blit-%(__version__)s.tar.gz' % locals(),
      license='BSD')
