from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=b'"Cm>\\\xaa\\L\x9b\xbek\xc6\xfa)\x98\x9f',
        DEBUG=True,
        # SQLALCHEMY_DATABASE_URI='sqlite:///database.db',
        # SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import main
    app.register_blueprint(main.bp)

    return app
