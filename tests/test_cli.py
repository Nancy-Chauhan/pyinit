import os
import tempfile
from pathlib import Path
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch

from pyinit import cli

package_name = "foobar"
version = "0.0.0"
author_name = "test"
author_email = "test@example.com"
description = "This is a sample package"
project_url = "http://example.com"


def create_mock_input(readme_type):
    def mock_input(s):
        if s == "Enter Python package name: ":
            return package_name
        elif s == "Enter Version number: ":
            return version
        elif s == "Enter author name: ":
            return author_name
        elif s == "Enter author email address: ":
            return author_email
        elif s == "Enter Description: ":
            return description
        elif s == "Enter Readme type ( markdown or rst ) : ":
            return readme_type
        elif s == "Enter Project URL: ":
            return project_url

    return mock_input


class TestCli(TestCase):
    maxDiff = None
    @patch('pyinit.cli.input')
    def test_main_crates_package_with_markdown_readme(self, mock_input):
        readme_file_name = "README.md"
        mock_input.side_effect = create_mock_input(readme_type="markdown")
        expected_readme = dedent(f"""
                        # {package_name}

                        {description}

                        ## Installation

                        ### Requirements

                        - python 3.6 +

                        ## Usage

                        ## Developing

                        ### Requirements
                        """.lstrip('\n'))
        self.assert_package_created(readme_file_name, expected_readme, "text/markdown")

    @patch('pyinit.cli.input')
    def test_main_crates_package_with_restructured_text_readme(self, mock_input):
        readme_file_name = "README.rst"
        mock_input.side_effect = create_mock_input(readme_type="rst")
        expected_readme = dedent(f"""
                        ######
                        {package_name}
                        ######

                        {description}

                        Installation
                        ************

                        Requirements
                        ============

                        Usage
                        *****

                        Developing
                        **********

                        Requirements
                        ============
                        """.lstrip('\n'))

        self.assert_package_created(readme_file_name, expected_readme, "text/x-rst")

    def assert_package_created(self, readme_file_name, expected_readme, readme_mime_type):
        with tempfile.TemporaryDirectory() as cwd:
            os.chdir(cwd)

            cli.main()

            pkg_root = Path(cwd)

            module_root = pkg_root.joinpath(package_name)
            test_root = pkg_root.joinpath('tests')
            readme = pkg_root.joinpath(readme_file_name)
            setup_py = pkg_root.joinpath('setup.py')

            self.assertTrue(pkg_root.is_dir())

            self.assertTrue(module_root.is_dir())
            self.assertTrue(test_root.is_dir())

            self.assertTrue(module_root.joinpath('__init__.py').is_file())
            self.assertTrue(test_root.joinpath('__init__.py').is_file())

            readme = readme.read_text()
            self.assertEqual(expected_readme, readme)

            actual_setup_py = setup_py.read_text()
            expected_setup_py = dedent(f"""
            import setuptools
            
            with open("{readme_file_name}", "r") as fh:
               long_description = fh.read()
            
            setuptools.setup(
               name="foobar",
               version="0.0.0",
               author="{author_name}",
               author_email="{author_email}",
               description="{description}",
               long_description=long_description,
               long_description_content_type="{readme_mime_type}",
               url="{project_url}",
               packages=setuptools.find_packages(),
               classifiers=[
                   "Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
               ]
            )
            """.lstrip('\n'))
            self.assertEqual(expected_setup_py, actual_setup_py)
