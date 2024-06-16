from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:   
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","") for r in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements



setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='pramod',
    author_email='pk1818202@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    packages= find_packages()
)        
