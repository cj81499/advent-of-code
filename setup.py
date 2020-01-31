from setuptools import setup, find_packages

setup(
    name="advent2019",
    packages=find_packages(
        exclude=("test", "*test*")
    ),
)
