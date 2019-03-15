# pylint: disable=unused-argument
def test_signup(app, db):
    client = app.test_client()
    result = client.post(
        '/api/user/signup',
        data=dict(
            username="shaibu", password="dummy", email="shaibu@gmail.com"
        ),
    )
    assert result.status_code == 200


# pylint: disable=unused-argument
def test_signin(app, db):
    client = app.test_client()
    signup_result = client.post(
        '/api/user/signup',
        data=dict(
            username="shaibujnr", password="dummy", email="shaibujnr@gmail.com"
        ),
    )
    assert signup_result.status_code == 200
    result = client.post(
        '/api/user/signin', data=dict(username="shaibujnr", password="dummy")
    )
    assert result.status_code == 200
