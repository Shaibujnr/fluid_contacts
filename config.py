class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    JWT_HEADER_TYPE = "JWT"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://zed:#1234@localhost/fluid_contacts"
    SECRET_KEY = "\xa7\xa5\x1c\x06\x1e\xd4z\xe1\xdeq\xf4\xbf\x1487\xcb\xa4\x0f7T\x19z\xe1'"
    JWT_SECRET_KEY = (
        "thisisadevelopmentsecretkeyforflaskjwtinprojectfluidcontacts"
    )
    DEBUG = True
    ENV = "development"


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    SECRET_KEY = (
        "_\xa0$ \x85\xec\xe4\xa4\xc9\x97\xe6\xb0Y\xd6,`\xb6sBs\xcey\xfd\xd9"
    )
    JWT_SECRET_KEY = "thisisatestsecretkeyforflaskjwtinprojectfluidcontacts"
    TESTING = True
    DEBUG = False
