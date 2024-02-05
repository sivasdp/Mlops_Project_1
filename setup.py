from setuptools import find_packages,setup
from typing import List

temp="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a requirements from "requirements.txt" as list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if temp in requirements:
            requirements.remove(temp)
    return requirements


setup(

    name="MLProject",
    version="0.0.1",
    author="SivaSDP",
    author_email="sdpsiva191@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)