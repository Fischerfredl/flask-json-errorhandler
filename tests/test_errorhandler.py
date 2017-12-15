import unittest
import json

import flask

from flask_json_errorhandler import init_errorhandler


default_messages = {
    400: 'The browser (or proxy) sent a request that this server could not understand.',
    401: 'The server could not verify that you are authorized to access the URL requested.  You either supplied the '
         'wrong credentials (e.g. a bad password), or your browser doesn\'t understand how to supply the credentials '
         'required.',
    403: 'You don\'t have the permission to access the requested resource. It is either read-protected or not readable '
         'by the server.',
    404: 'The requested URL was not found on the server.  If you entered the URL manually please check your spelling '
         'and try again.',
    405: 'The method is not allowed for the requested URL.',
    409: 'A conflict happened while processing the request.  The resource might have been modified while the request '
         'was being processed.',
    410: 'The requested URL is no longer available on this server and there is no forwarding address. If you followed '
         'a link from a foreign page, please contact the author of this page.',
    500: 'internal server error'
}


class TestErrorhandler(unittest.TestCase):
    def setupRoutes(self, code, extended=True):
        """setup routes that return the given errorcode

        "/": default abort
        "/custom": abort with message "custom message"
        """

        @self.app.route('/')
        def index():
            return flask.abort(code)

        if extended:
            @self.app.route('/custom')
            def custom():
                return flask.abort(code, 'custom message')

    def assertResponse(self, code, extended=True):
        """assert the above routes behave as expected"""

        # check default route
        response = self.client.get('/')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, code)
        self.assertTrue(isinstance(data, dict))

        self.assertEqual(default_messages[code], data['error'])

        # check custom message
        if extended:
            response = self.client.get('/custom')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, code)
            self.assertTrue(isinstance(data, dict))
            self.assertIn('custom message', data['error'])

    def setUp(self):
        self.app = flask.Flask(__name__)

        init_errorhandler(self.app)

        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_bad_request(self):
        self.setupRoutes(400)
        self.assertResponse(400)

    def test_unathorized(self):
        self.setupRoutes(401)
        self.assertResponse(401)

    def test_forbidden(self):
        self.setupRoutes(403)
        self.assertResponse(403)

    def test_not_found(self):
        self.setupRoutes(404)
        self.assertResponse(404)

    def test_not_allowed(self):
        self.setupRoutes(405, extended=False)
        self.assertResponse(405, extended=False)

    def test_conflict(self):
        self.setupRoutes(409)
        self.assertResponse(409)

    def test_conflict(self):
        self.setupRoutes(410)
        self.assertResponse(410)

    def test_internal_server_error(self):
        self.setupRoutes(500, extended=False)
        self.assertResponse(500, extended=False)
