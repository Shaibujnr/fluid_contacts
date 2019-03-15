from fluid_contacts.models import User


def test_new_user():
    user = User(
        username="shaibu", email="shaibu@gmail.com", password="testpassword"
    )
    assert user is not None
    assert user.password == "testpassword"
    assert user.username == "shaibu"
    assert user.email == "shaibu@gmail.com"


def test_user_hash_password():
    user = User(username="shaibu", email="shaibu@gmail.com", password="test")
    assert user.password == "test"
    user.set_password("test")
    assert user.password != "test"
    assert user.verify_password("test")
    assert not user.verify_password("wrong")
