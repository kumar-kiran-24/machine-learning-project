from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT = "-e"

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [req.strip() for req in requirements]  # Remove whitespace/newlines
    if HYPHEN_DOT in requirements:
        requirements.remove(HYPHEN_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="kiran",
    author_email="kirankumar26650@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
