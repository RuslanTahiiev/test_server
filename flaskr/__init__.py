from flask import Flask


def init_app():
    app = Flask(__name__,
                static_folder='static',
                )
    app.config.from_object('config.Config')

    # Init plugins

    with app.app_context():
        from .routes import index

        return app
