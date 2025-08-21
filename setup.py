from setuptools import find_packages, setup
from typing import List
import sys

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) ->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

sys.path.append("D:/GitHub/Hanoi-House-Price-Prediction/src")

setup(
    name = 'hanoi-house-price-prediction',
    version = '0.0.1',
    author='Nhat Anh NT',
    author_email='stephen.ca.work@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirement.txt')
)