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
