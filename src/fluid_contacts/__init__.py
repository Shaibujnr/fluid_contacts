import os
from flask import Flask
from .models import db


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig",
}


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
    return app


__version__ = "0.1.0"
