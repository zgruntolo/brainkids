#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    author="Tommaso Seremia",
    author_email="t.seremia@gmail.com",
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "brain_kids=brain_kinds.main",
        ],
    },
    keywords="brainkids",
    name="brainkids",
    description="BrainKids",
    packages=find_packages(include=["brain_kids"]),
    test_suite="tests",
    url="https://github.com/zgruntolo/brainkids",
    version="1.0.0",
)