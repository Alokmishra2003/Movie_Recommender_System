from setuptools import setup, find_packages

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define package metadata
AUTHOR_NAME = 'ALOK MISHRA'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

# Setup function call
setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='alokmishra0504@gmail.com',
    description='A package for movie recommender',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Corrected to use find_packages() if you want to automatically find packages
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)
