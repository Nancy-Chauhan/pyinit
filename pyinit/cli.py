import pathlib

from pyinit import setup_template
from pyinit.readme_template import render_md, render_rst


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
        readme_file = "README.md"
        readme_text = render_md(package_name, description)
    else:
        readme_file = "README.rst"
        readme_text = render_rst(package_name, description)

    cwd.joinpath(readme_file).write_text(readme_text)

    cwd.joinpath("setup.py").write_text(
        setup_template.render(readme_file, package_name, version, author, author_email, description, url))
