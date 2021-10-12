from setuptools import setup, find_packages
setup(
    name="gdcli",
    version="1.0.3",
    author="Subrahmanya s hegade",
    author_email="hegadedevelopment@gmail.com",
    description="Command line too used for simple google dorks",
    packages=find_packages(include=['gdcli', 'gdcli.*']),
    entry_points='''
    [console_scripts]
    gdcli=gdcli.gd:start
    '''

)
