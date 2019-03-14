import os
import pytest


@pytest.fixture
def app():
    from fluid_contacts import create_app

    os.environ["FLASK_CONFIGURATION"] = "testing"
    app = create_app()
    assert app is not None
    assert app.config["TESTING"]
    return app


@pytest.fixture
def db(app):
    from flask_sqlalchemy import SQLAlchemy
    from fluid_contacts.models import metadata

    db = SQLAlchemy(app, metadata=metadata)
    db.create_all()
    return db
