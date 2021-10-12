from setuptools import setup,find_packages
setup(
    name="src",
    version="1.0.0",
    packages=find_packages(include=['src', 'src.*']),
    
   
    entry_points='''
    [console_scripts]
    gd=src.gd:start
    '''

)