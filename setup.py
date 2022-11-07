from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requiurment_list:List[str] = []
    return requiurment_list

setup(

    name="sensor",
    version="0.0.1",
    author="harish",
    author_email="harishrog24@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"]
)