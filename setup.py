from setuptools import setup

setup(
    name='ljout',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/ljout'],

    requires=['termtool'],
    install_requires=['termtool'],
)
