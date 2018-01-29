from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='flask-json-errorhandler',
    version='1.0.3',
    description='Register json errorhandlers for a flask REST server',
    long_description=readme(),
    url='https://github.com/fischerfredl/flask-json-errorhandler',
    author='Alfred Melch',
    author_email='alfred.melch@gmx.de',
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['flask', 'json', 'errorhandler'],
    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=['flask>=0.12.2'],
    test_suite='tests.test_suite',
    tests_require=[],
)
