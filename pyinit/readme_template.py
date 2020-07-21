from textwrap import dedent


def render_md(title, description):
    return dedent(f"""
    # {title}
    
    {description}
    """.lstrip('\n'))


def render_rst(title, description):
    heading_sep = '#' * len(title)
    return dedent(f"""
    {heading_sep}
    {title}
    {heading_sep}
    
    {description}
    """.lstrip('\n'))
