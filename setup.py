# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MyLambData", # the name that you will install via pip
    version="1.0",
    author="Griffin Wilson",
    author_email="wilson.griffin15@gmail.com",
    description="A short description example",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/Griffinw15/MyLambData",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)