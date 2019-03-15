import json


def test_add_contact(app, token):
    client = app.test_client()
    result = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    data = json.loads(result.data.decode())
    contact_id = data.get('id', None)
    assert contact_id is not None


def test_read_all_contact(app, token):
    client = app.test_client()
    result_contact_one = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_contact_one.status_code == 200
    result_contact_two = client.post(
        "/api/contact",
        data=dict(
            name="John Doe",
            phonenumber="08000000001",
            email="remail@gmail.com",
            address="#5 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_contact_two.status_code == 200
    result = client.get(
        '/api/contact', headers={"Authorization": "JWT %s" % token}
    )
    assert result.status_code == 200
    data = json.loads(result.data.decode())
    assert isinstance(data, list)
    assert len(data) == 2
