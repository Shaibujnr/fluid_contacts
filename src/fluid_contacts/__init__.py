import os
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

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


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(
        config[config_name]
    )  # object-based default configuration
    app.config.from_pyfile(
        "config.cfg", silent=True
    )  # instance-folders configuration


metadata = MetaData(naming_convention=convention)
app = Flask(__name__)
configure_app(app)
db = SQLAlchemy(app, metadata=metadata)


@app.route("/")
def hello():
    print(app.config)
    return "<h1>Hello world</h1>"


def create_app():
    return app


__version__ = "0.1.0"
