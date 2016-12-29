"""The setup for Mailroom distribution."""

from setuptools import setup

requires = [
    'gevent'
]

setup(
    name='http-server',
    description='Setting up an HTTP-Server.',
    version=0.1,
    author='Sera Smith, Julien Wilson',
    author_email='seras37@gmail.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['server', 'client', 'con_server'],
    install_requires=requires,
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
         'console_scripts': [
            "server = server:build_server",
            "client = client:main",
            "con_server = con_server:main"
         ]
    }
)
