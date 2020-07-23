from textwrap import dedent
from unittest import TestCase

from pyinit.readme_template import render_md, render_rst


class Test(TestCase):
    def test_render_md_should_generate_readme_in_markdown(self):
        readme = render_md('test', 'This is a description')

        expected = dedent("""
        # test

        This is a description

        ## Installation

        ### Requirements

        - python 3.6 +

        ## Usage

        ## Developing

        ### Requirements
        """.lstrip('\n'))
        self.assertEqual(expected, readme)

    def test_render_rst_should_generate_readme_in_restructured_text(self):
        readme = render_rst('test', 'This is a description')

        expected = dedent("""
        ####
        test
        ####
        
        This is a description
        """.lstrip('\n'))
        self.assertEqual(expected, readme)
