from setuptools import setup, find_packages
setup(
    name="gd",
    version="1.0.0",
    author="Subrahmanya s hegade",
    description="Command line too used for simple google dorks",
    packages=find_packages(include=['src', 'src.*']),
    entry_points='''
    [console_scripts]
    gd=src.gd:start
    '''

)
