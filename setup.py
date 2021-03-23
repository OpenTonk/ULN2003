import setuptools
from setuptools import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ULN2003-OpenTonk",
    version="0.0.1",
    author="Neo Hop",
    author_email="neotje111@gmail.com",
    description="stepper driver library for the ULN2003 chip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenTonk/ULN2003",
    project_urls={
        "Bug Tracker": "https://github.com/OpenTonk/ULN2003/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)