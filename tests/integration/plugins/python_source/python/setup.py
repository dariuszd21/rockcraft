# noqa: INP001 (implicit namespace package)
from setuptools import setup

setup(
    name="hello",
    version="0.1",
    entry_points={"console_scripts": ["hello=hello.__main__:main"]},
    packages=["hello"],
)
