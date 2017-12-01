from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read


setup(
    name='json-errorhandler',
    description='Register json errorhandlers for a flask REST server',
    long_description=readme(),
    url='https://qgit.de/qerida/py-lib/flask_json_errorhandler',

    version='0.1',
    licence='UNLICENSED',

    author='Alfred Melch',
    author_email='alfred.melch@gmx.de',

    packages=find_packages(exclude=['tests.*', 'tests']),

    # dependencies
    install_requires=['flask'],
    dependency_links=[],

    test_suite='tests.test_suite',
    tests_require=[],
)
