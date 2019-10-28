#!/usr/bin/env python3
import os
import setuptools

INSTALL_REQUIRES = ['numpy', 'pandas', 'mountainlab-pytools']
TESTS_REQUIRE = ['pytest >= 2.7.1']

base_dir = os.path.dirname(os.path.abspath(__file__))

setuptools.setup(
    name='rec_to_binaries',
    setup_requires=["wheel"],
    version='0.1.1.dev0',
    license='MIT',
    description=('Covert SpikeGadgets rec files to binaries'),
    author='Eric Denovellis, Daniel Liu',
    author_email='Eric.Denovellis@ucsf.edu',
    url='https://github.com/wbodo/rec_to_binaries',
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
)
