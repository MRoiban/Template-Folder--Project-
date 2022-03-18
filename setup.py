from setuptools import setup
setup(
    name='create',
    version='0.0.1',
    py_modules = ['os', 'sys'],
    entry_points={
        'console_scripts': [
            'create=create:main'
        ]
    }
)