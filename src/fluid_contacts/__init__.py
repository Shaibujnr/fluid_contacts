import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig",
}

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
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
    from .api import blueprint

    app = Flask(__name__)
    configure_app(app)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(blueprint, url_prefix="/api")
    return app


__version__ = "0.1.0"
