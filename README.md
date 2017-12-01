[![pipeline status](https://qgit.de/py-lib/flask-json-errorhandler/badges/master/pipeline.svg)](https://qgit.de/py-lib/flask-json-errorhandler/commits/master)
[![coverage report](https://qgit.de/py-lib/flask-json-errorhandler/badges/master/coverage.svg)](https://qgit.de/py-lib/flask-json-errorhandler/commits/master)

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
Normal:
```python
python setup.py test
```

For coverage use the python coverage package. See ```/cov.sh``` for usage. 

```./cov.sh``` will pip install coverage. So make sure to use it in the context of your virtual env.
