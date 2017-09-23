"""A setuptools based setup module.

@author: olinox14, 2017
"""

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='xdice',

    version='1.1.3',

    description='The swiss knife for Dice roll : Command line, API (documented!), advanced dice notation parser, compilable patterns...etc.',
    long_description=long_description,

    url='https://github.com/cro-ki/xdice',

    author='Olivier Massot',
    author_email='croki.contact@gmail.com',

    license='GNU',

    py_modules=['xdice', 'roll'],
    python_requires='>=3.3',

    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        "Intended Audience :: Other Audience",
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Role-Playing',
        'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
        'Topic :: Games/Entertainment :: Turn Based Strategy',

        'License :: OSI Approved :: GNU General Public License (GPL)',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='xdice roll d20 game random parser dices role board',

)
