import setuptools
from distutils.core import run_setup

with open("README.md","r") as fh:
    long_des = fh.read()

setuptools.setup(name = "battleship_pkg_at970",
                 version = "0.0.1",
                 author = "Angelo Singh Thind",
    author_email= "at970@exeter.ac.uk",
    description= "A python implementation of battleship board game",
    long_description= long_des,
    url = "https://github.com/angelothind/Battleship-project.git",
    classifiers= [
        'Programming Language :: Python :: 3.9'
        'License :: OSI Approved :: MIT License'],
    python_requires = '>=3.9')


run_setup('setup.py', script_args=['sdist'])