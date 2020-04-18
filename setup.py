from setuptools import setup

setup(
    name='Price',
    version='0.1.0',
    py_modules=['price', 'price'],
    install_requires=[
        'click',
        'mechanicalsoup'
    ],
    entry_points='''
        [console_scripts]
        price=price.cli:price
    '''
)
