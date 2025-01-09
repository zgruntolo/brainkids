#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    author="Tommaso Seremia",
    author_email="t.seremia@gmail.com",
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "livingornot=livingornot.main",
        ],
    },
    keywords="livingornot",
    name="livingornot",
    description="Living Or Not",
    packages=find_packages(include=["livingornot.src", "livingornot.src.*"]),
    #test_suite="tests",
    url="https://github.com/Team-PyPo/nexus-novel",
    version="0.0.1",
)