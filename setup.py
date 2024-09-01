from typing import List
from setuptools import setup,find_packages
import os
# For a list of other possible classifiers, see
# http://pypi.python.org/pypi?%3Aaction=list_classifiers

HYPON_E_DOT ='-e .'

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath, 'r') as f:
        requirements=f.readline()
        requirements = [i.replace('\n','') for i in requirements]
        if HYPON_E_DOT in requirements:
            requirements.remove(HYPON_E_DOT)



setup(
    name='ml-project-pipeline-price',
    version='0.1.0',
    description='ml project pipeline price prdiction',
    url='https://github.com/Zain-art/price-prediction-mlp',
    author='zain khan',
    author_email='zainprogrammers@gmail.com',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)