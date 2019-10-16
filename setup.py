import pypandoc

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Convert the README.md to README.rst
with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO: Change the following variables to match your app
app_name = 'alembic-multischema'

# Versions should comply with PEP440.  For a discussion on single-sourcing
# the version across setup.py and the project code, see
# https://packaging.python.org/en/latest/single_source_version.html
app_version = '0.0.5'

app_description = 'Multi schema postgres migrations using alembic'

# How mature is this project? Common values are
#   3 - Alpha
#   4 - Beta
#   5 - Production/Stable
app_dev_status = '3 - Alpha'

# What does your project relate to?
app_keywords = 'quinovas'

# List run-time dependencies here.  These will be installed by pip when
# your project is installed. For an analysis of "install_requires" vs pip's
# requirements files see:
# https://packaging.python.org/en/latest/requirements.html
app_install_requires = []


setup(
    name=app_name,

    version=app_version,

    description=app_description,
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/QuiNovas/alembic-multischema',

    author='Mathew Moon',
    author_email='me@mathewmoon.net',

    license='APL 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: '+app_dev_status,

        # Indicate who your project is intended for
        'Topic :: System :: Software Distribution',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords=app_keywords,

    install_requires=app_install_requires,

    package_dir={'': 'src'},
    packages=find_packages('src'),

    setup_requires=['pypandoc'],
)
