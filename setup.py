# -*- coding: utf-8 -*-
import re
from os import path
from setuptools import setup

ROOT_DIR = path.abspath(path.dirname(__file__))

DESCRIPTION = 'Flask-TuiEditor - a Flask extension for TuiEditor'
LONG_DESCRIPTION = open(path.join(ROOT_DIR, 'README.md')).read()
VERSION = re.search(
    "__version__ = '([^']+)'",
    open(path.join(ROOT_DIR, 'flask_tuieditor', '__init__.py')).read()
).group(1)


setup(
    name='Flask-TuiEditor',
    version=VERSION,
    url='https://github.com/pyx/flask-tuieditor/',
    license='MIT',
    author='Anton gavrilyuk',
    author_email='amigoalt@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['flask_tuieditor'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
    ],
    extras_require={
        'test': ['pytest>=2.8.2'],
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
