[![version](https://img.shields.io/pypi/v/flask-json-errorhandler.svg)](https://pypi.python.org/pypi/flask-json-errorhandler)
[![license](https://img.shields.io/pypi/l/flask-json-errorhandler.svg)](https://pypi.python.org/pypi/flask-json-errorhandler)
[![pyversions](https://img.shields.io/pypi/pyversions/flask-json-errorhandler.svg)](https://pypi.python.org/pypi/flask-json-errorhandler)
[![pipeline status](https://travis-ci.org/Fischerfredl/flask-json-errorhandler.svg?branch=master)](https://travis-ci.org/Fischerfredl/flask-json-errorhandler)
[![coverage](https://img.shields.io/codecov/c/github/fischerfredl/flask-json-errorhandler.svg)](https://codecov.io/gh/Fischerfredl/flask-json-errorhandler)

# flask-json-errorhandler
Register json errorhandlers for a flask REST server

## Usage

```python 
from flask import Flask

from flask_json_errorhandler import init_errorhandler(app)


def create_app():
    app = Flask(__name__)
    init_errorhandler(app)
```

## Testing
```python
python setup.py test
```
