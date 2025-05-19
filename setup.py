from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e.'
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    from a requirements.txt file.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='end_to_end_ml',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Esteban G.',
    author_email= "estebangomezz@hotmail.com",
    description='This a project example of how to make an end to end machine learning model'
)