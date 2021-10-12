from setuptools import setup, find_packages
setup(
    name="gdcli",
    version="1.0.5",
    author="Subrahmanya s hegade",
    author_email="hegadedevelopment@gmail.com",
    description='''
    Command line too used for simple google dorks
    ''',
    long_description='''
             Usage
             1) -op 1 for general query \n
              >> gd -op 1 -q ninja -s instagram -e gamer \n
             2) -op 2 for instagram user finding
              >> gd -op 2 -q ninja -b gamer -l usa
            

    ''',
    packages=find_packages(include=['gdcli', 'gdcli.*']),
    entry_points='''
    [console_scripts]
    gdcli=gdcli.gd:start
    '''

)
