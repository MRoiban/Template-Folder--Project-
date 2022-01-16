from setuptools import setup
setup(
    name='project',
    version='0.0.1',
    py_modules = ['os', 'sys'],
    entry_points={
        'console_scripts': [
            'project=project:main'
        ]
    }
)