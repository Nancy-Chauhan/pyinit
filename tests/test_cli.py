import os
import tempfile
from pathlib import Path
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch

from pyinit import cli


class TestCli(TestCase):
    @patch('pyinit.cli.input')
    def test_main_generates_project_with_markdown_readme(self, mock_input):
        package_name = "foobar"
        version = "0.0.0"
        author_name = "test"
        author_email = "test@example.com"
        description = "This is a sample package"
        project_url = "http://example.com"
        readme_file_name = 'README.md'

        def input_side_effects(s):
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
                return "markdown"
            elif s == "Enter Project URL: ":
                return project_url

        mock_input.side_effect = input_side_effects

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

            self.assertTrue(readme.is_file())

            self.assertTrue(module_root.joinpath('__init__.py').is_file())
            self.assertTrue(test_root.joinpath('__init__.py').is_file())

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
               long_description_content_type="text/markdown",
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
