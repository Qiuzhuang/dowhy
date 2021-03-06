"""A setuptools based setup module for dowhy.

Adapted from:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the required packages
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = f.read().splitlines()

# Loading version number
with open(path.join(here, 'dowhy', 'VERSION')) as version_file:
    version = version_file.read().strip()
    print(version)

setup(
    name='dowhy',
    version=version,
    description='DoWhy is a Python library for causal inference that supports explicit modeling and testing of causal assumptions.',  # Required
    license='MIT',
    long_description=long_description,
    url='https://github.com/microsoft/dowhy',  # Optional
    download_url='https://github.com/microsoft/dowhy/archive/v0.5.tar.gz',
    author='Amit Sharma, Emre Kiciman',
    classifiers=[  # Optional
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='causality machine-learning causal-inference statistics graphical-model',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.5',
    install_requires=install_requires,
    include_package_data=True,
    package_data={'dowhy':['VERSION']}
)
