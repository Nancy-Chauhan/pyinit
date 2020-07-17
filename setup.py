import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyinit",
    version="0.0.1",
    author="Nancy Chauhan",
    author_email="nancychn1@gmail.com",
    description="Tool to create python project structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nancy-Chauhan/pyinit",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pyinit = pyinit.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
