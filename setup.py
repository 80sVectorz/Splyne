from setuptools import setup, find_packages

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='splyne',
    version='0.0.1',
    description='Splyne the package for all you spline related needs',
    long_description=long_description,
    license="MIT",
    url='https://github.com/80sVectorz/splyne',
    author='80sVectorz',
    package_dir={'':'src'},
    packages=["splyne"],
    classifiers=['Development Status :: 1 - Planning'],
)