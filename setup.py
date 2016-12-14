"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='http-server',
    description='Setting up an HTTP-Server.',
    version=0.1,
    author='Sera Smith, Julien Wilson',
    author_email='seras37@gmail.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['server', 'client'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
         'console_scripts': [
            "server = server:main",
            "client = client:main"
         ]
    }
)
