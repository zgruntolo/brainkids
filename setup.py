#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    author="Tommaso Seremia",
    author_email="t.seremia@gmail.com",
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "livingornot=livingornot.main",
        ],
    },
    keywords="schooltestsuite",
    name="schooltestsuite",
    description="School Test Suite",
    packages=find_packages(include=["schooltestsuite", "livingornot.*"]),
    #test_suite="tests",
    url="https://github.com/Team-PyPo/nexus-novel",
    version="1.0.1",
)