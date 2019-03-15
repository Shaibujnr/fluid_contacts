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


def test_contact(db):
    user = User(username="shaibu", email="shaibu@gmail.com", password="test")
    db.session.add(user)
    db.session.commit()
    contact = Contact(
        phonenumber="080", email="c@gmail.com", address="home", user_id=user.id
    )
    contact2 = Contact(
        phonenumber="090",
        email="c1@gmail.cmo",
        address="house",
        user_id=user.id,
    )
    db.session.add(contact)
    db.session.add(contact2)
    assert user.id is not None
    assert len(user.contacts) == 2
