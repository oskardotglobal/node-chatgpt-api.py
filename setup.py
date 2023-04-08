import subprocess

from setuptools import find_packages
from setuptools import setup

setup(
    name="node_chatgpt_api",
    version="1.0.0",
    license="MIT",
    author="Oskar Manhart",
    author_email="me@oskar.global",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/oskardotglobal/node-chatgpt-api.py",
    install_requires=subprocess.check_output(["pip", "freeze"]).decode().split("\n"),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
