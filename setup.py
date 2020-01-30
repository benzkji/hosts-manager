from setuptools import setup


# hope this works
# http://click.pocoo.org/5/setuptools/#scripts-in-packages
setup(
    name='hosts manager',
    version='0.1',
    py_modules=['hosts', ],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        hosts=hosts:hosts_manager
    ''',
)