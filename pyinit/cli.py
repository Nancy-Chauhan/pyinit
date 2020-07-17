import pathlib

from pyinit import setup_template


def main():
    package_name = input("Enter Python package name: ")
    version = input("Enter Version number: ")
    author = input("Enter author name: ")
    author_email = input("Enter author email address: ")
    description = input("Enter Description: ")
    readme = input("Enter Readme type ( markdown or rst ) : ")
    url = input("Enter Project URL: ")

    cwd = pathlib.Path.cwd()
    package = cwd.joinpath(package_name)
    package.mkdir()
    tests = cwd.joinpath("tests")
    tests.mkdir()
    package.joinpath("__init__.py").touch()
    tests.joinpath("__init__.py").touch()
    if readme == "markdown":
        cwd.joinpath("README.md").touch()
    else:
        cwd.joinpath("README.rst").touch()
    cwd.joinpath("setup.py").write_text(
        setup_template.template(readme, package_name, version, author, author_email, description, url))
