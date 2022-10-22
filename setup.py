from setuptools import setup, find_packages

from lib_now import __version__

setup(
    name='lib_now',
    version=__version__,

    url='https://github.com/baender/test_python_ibs',
    author='Baender',

    packages=find_packages(),
)
