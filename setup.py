from setuptools import setup, find_packages

setup(
    name="pongo-python",
    version="4.0.0",
    packages=find_packages(),
    description="A Python package for interacting with the Pongo API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Caleb John",
    author_email="caleb.john@joinpongo.com",
    url="https://github.com/PongoAI/pongo-python",
    install_requires=[
        "requests",  # Include any other dependencies your package needs
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="Apache 2.0",  # Your package's license
)
