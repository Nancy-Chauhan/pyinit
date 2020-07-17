import os
import tempfile
from unittest import TestCase
from unittest.mock import patch

from pyinit import cli


class TestCli(TestCase):

    @patch('pyinit.cli.input')
    def test_main(self, mock_input):
        def input_side_effects(s):
            if s == "Enter Python package name: ":
                return "Test"
            elif s == "Enter Version number: ":
                return "0.0.0"
            elif s == "Enter author name: ":
                return "test"
            elif s == "Enter author email address: ":
                return "test@example.com"
            elif s == "Enter Description: ":
                return "This is test"
            elif s == "Enter Readme type ( markdown or rst ) : ":
                return "markdown"
            elif s == "Enter Project URL: ":
                return "http://example.com"

        mock_input.side_effect = input_side_effects

        with tempfile.TemporaryDirectory() as cwd:
            os.chdir(cwd)

            cli.main()

            os.path.isdir(cwd + "/tests")
            os.path.isdir(cwd + "/Test")
            os.path.isfile(cwd + "/Test/__init__.py")
            os.path.isfile(cwd + "/tests/__init__.py")
            os.path.isfile(cwd + "/README.md")

            with open(cwd + "/setup.py") as file:
                setup_py = file.read()
                expected_output = """import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
   name="Test", # Replace with your own username
   version="0.0.0",
   author="test",
   author_email="test@example.com",
   description="This is test",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="http://example.com",
   packages=setuptools.find_packages(),
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ]
)
"""
                self.maxDiff = None
                self.assertEqual(expected_output, setup_py)
