"""setup.py for boilerplate-sdk"""
# pylint: disable=E0611,F0401
#         No name 'core' in module 'distutils'
#         Unable to import 'distutils.core'
from distutils.core import setup
import setuptools # pylint: disable=unused-import
setup(name='boilerplate-sdk',
      version='0.1.0',
      license='MIT',
      author='hshaosf',
      author_email='hshaosf@SFDigitalServices',
      url='https://github.com/SFDigitalServices',
      packages=["boilerplate_sdk"],
      install_requires=[
          'requests'
      ]
      )
