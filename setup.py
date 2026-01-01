from setuptools import setup, find_packages

setup(
    name="hakiix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="daimondz",
    description="Hakiix console logger module",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daimondz2/hakiix",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)