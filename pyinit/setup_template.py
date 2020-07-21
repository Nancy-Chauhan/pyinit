from textwrap import dedent


def render(readme, package_name, version, author, author_email, description, url):
    return dedent(f"""
    import setuptools
    
    with open("{readme}", "r") as fh:
       long_description = fh.read()
    
    setuptools.setup(
       name="{package_name}",
       version="{version}",
       author="{author}",
       author_email="{author_email}",
       description="{description}",
       long_description=long_description,
       long_description_content_type="text/markdown",
       url="{url}",
       packages=setuptools.find_packages(),
       classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
       ]
    )
    """.lstrip('\n'))
