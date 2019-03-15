import os
import json
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
    from fluid_contacts import db

    with app.app_context():
        db.drop_all()
        db.create_all()


@pytest.fixture
def token(app, db):
    client = app.test_client()
    result = client.post(
        '/api/user/signup',
        data=dict(
            username="randomusername",
            password="randompassword",
            email="randomemail@gmail.com",
        ),
    )
    assert result.status_code == 200
    data = json.loads(result.data.decode())
    token = data.get('token', None)
    assert token is not None
    return token
