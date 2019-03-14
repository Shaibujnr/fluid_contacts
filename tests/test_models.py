from fluid_contacts.models import User, Contact


def test_new_user():
    user = User(
        username="shaibu", email="shaibu@gmail.com", password="testpassword"
    )
    assert user is not None
    assert user.password == "testpassword"
    assert user.username == "shaibu"
    assert user.email == "shaibu@gmail.com"


def test_add_user(db):
    user = User(username="Shaibu", email="s@gmail.com", password="test")
    assert user.id is None
    db.session.add(user)
    db.session.commit()
    assert user.id is not None


def test_user_hash_password():
    user = User(username="shaibu", email="shaibu@gmail.com", password="test")
    assert user.password == "test"
    user.set_password("test")
    assert user.password != "test"
    assert user.verify_password("test")
    assert not user.verify_password("wrong")


def test_contact():
    user = User(username="shaibu", email="shaibu@gmail.com", password="test")
    contact = Contact(phonenumber="080", email="c@gmail.com", address="home")
    assert user is not None
    assert contact is not None
    # user.contacts.append(contact)
