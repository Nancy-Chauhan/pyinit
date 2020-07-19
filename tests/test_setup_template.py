import unittest
from textwrap import dedent

from pyinit.setup_template import render


class TestSetupTemplate(unittest.TestCase):

    def test_render_should_generate_setup_py(self):
        actual_output = render(readme="README.md", package_name="Test", version="0.0.0", author="test",
                               author_email="test@example.com",
                               description="This is test", url="http://example.com")
        expected_output = dedent("""
        import setuptools
        
        with open("README.md", "r") as fh:
           long_description = fh.read()
        
        setuptools.setup(
           name="Test",
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
        """.lstrip('\n'))
        self.assertEqual(expected_output, actual_output)
