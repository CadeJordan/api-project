
from setuptools import setup, find_packages
from tft.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='tft',
    version=VERSION,
    description='TFT Utils',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Cade Jordan',
    author_email='cade.m.jordan@gmail.com',
    url='localhost',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'tft': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        tft = tft.main:main
    """,
)
