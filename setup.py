from setuptools import find_packages, setup

setup(
    name="advent-of-code-cj81499",
    version="0.0.1",
    description="cj81499's solutions for https://adventofcode.com/",
    url="https://github.com/cj81499/advent-of-code-cj81499",
    author="Cal Jacobson",
    # author_email="cj81499@example.com",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        "python-dotenv >= 0.15.0"
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(where=".", exclude="tests"),
    entry_points={
        "adventofcode.user": ["cj81499 = advent:solve"],
    },
)
