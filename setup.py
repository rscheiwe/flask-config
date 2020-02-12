from distutils.core import setup
from setuptools import find_packages

setup(
    name="insight",
    version='1.0',
    py_modules=['insight'],
    packages=find_packages(),

    # metadata
    author='Richard Scheiwe',
    author_email='richard.s@taboola.com',
    description='Insight API',
    license='Public domain',
    keywords='analysis',
)