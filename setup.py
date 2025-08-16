from setuptools import setup,find_packages
from typing import List

Hyphen_E_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"") for req in requirements]
    if Hyphen_E_dot in requirements:
        requirements.remove(Hyphen_E_dot)
    return requirements


setup(
    name='ML_Project',
    version='0.0.1',
    author='Mehul Gupta',
    author_email='mehulgupta2409@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)