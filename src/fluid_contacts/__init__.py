import os
from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db, User
from .api import blueprint


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig",
}

jwt = JWTManager()


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(
        config[config_name]
    )  # object-based default configuration
    app.config.from_pyfile(
        "config.cfg", silent=True
    )  # instance-folders configuration


def create_app():
    app = Flask(__name__)
    configure_app(app)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(blueprint, url_prefix="/api")
    return app


__version__ = "0.1.0"
