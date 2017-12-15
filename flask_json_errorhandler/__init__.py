from flask import make_response, jsonify


def init_errorhandler(app):
    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'error': error.description}), 400)

    @app.errorhandler(401)
    def unauthorized(error):
        return make_response(jsonify({'error': error.description}), 401)

    @app.errorhandler(403)
    def forbidden(error):
        return make_response(jsonify({'error': error.description}), 403)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': error.description}), 404)

    @app.errorhandler(405)
    def not_allowed(error):
        return make_response(jsonify({'error': error.description}), 405)

    @app.errorhandler(409)
    def conflict(error):
        return make_response(jsonify({'error': error.description}), 409)

    @app.errorhandler(410)
    def gone(error):
        return make_response(jsonify({'error': error.description}), 410)

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify({'error': 'internal server error'}), 500)
