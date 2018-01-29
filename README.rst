|version| |license| |pyversions| |pipeline status| |coverage|

flask-json-errorhandler
=======================

Register json errorhandlers for a flask REST server

Usage
-----

.. code:: python

    from flask import Flask

    from flask_json_errorhandler import init_errorhandler(app)


    def create_app():
        app = Flask(__name__)
        init_errorhandler(app)

Testing
-------

.. code:: python

    python setup.py test

.. |version| image:: https://img.shields.io/pypi/v/flask-json-errorhandler.svg
   :target: https://pypi.python.org/pypi/flask-json-errorhandler
.. |license| image:: https://img.shields.io/pypi/l/flask-json-errorhandler.svg
   :target: https://pypi.python.org/pypi/flask-json-errorhandler
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/flask-json-errorhandler.svg
   :target: https://pypi.python.org/pypi/flask-json-errorhandler
.. |pipeline status| image:: https://travis-ci.org/Fischerfredl/flask-json-errorhandler.svg?branch=master
   :target: https://travis-ci.org/Fischerfredl/flask-json-errorhandler
.. |coverage| image:: https://img.shields.io/codecov/c/github/fischerfredl/flask-json-errorhandler.svg
   :target: https://codecov.io/gh/Fischerfredl/flask-json-errorhandler
