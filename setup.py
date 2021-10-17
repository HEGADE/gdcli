from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="gdcli",
    version="1.0.7",
    author="Subrahmanya s hegade",
    author_email="hegadedevelopment@gmail.com",
    description='''
    Command line too used for simple google dorks
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['gdcli', 'gdcli.*']),
    entry_points='''
    [console_scripts]
    gdcli=gdcli.gd:start
    '''

)
