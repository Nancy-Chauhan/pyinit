from textwrap import dedent


def render_md(title, description):
    return dedent(f"""
    # {title}
    
    {description}

    ## Installation

    ### Requirements

    - python 3.6 +

    ## Usage

    ## Developing

    ### Requirements
    """.lstrip('\n'))


def render_rst(title, description):
    heading_sep = '#' * len(title)
    return dedent(f"""
    {heading_sep}
    {title}
    {heading_sep}
    
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
