from fluid_contacts import __version__
from fluid_contacts import create_app


def test_version():
    assert __version__ == '0.1.0'


def test_app_config():
    import os

    os.environ["FLASK_CONFIGURATION"] = "testing"
    app = create_app()
    assert app.config.get("TESTING")
    assert (
        app.config.get("SQLALCHEMY_DATABASE_URI")
        == "postgresql://zed:#1234@localhost/fluid_contacts_test"
    )
