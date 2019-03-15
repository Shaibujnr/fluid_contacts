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


def test_read_single_contact(app, token):
    client = app.test_client()
    result_add_contact = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_add_contact.status_code == 200
    data = json.loads(result_add_contact.data.decode())
    contact_id = data.get('id')
    assert contact_id is not None
    result = client.get(
        '/api/contact/%d' % contact_id,
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id


def test_edit_contact(app, token):
    client = app.test_client()
    result_add_contact = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_add_contact.status_code == 200
    data = json.loads(result_add_contact.data.decode())
    contact_id = data.get('id')
    assert contact_id is not None
    result = client.patch(
        '/api/contact/%d' % contact_id,
        data={"name": "Janet Doe"},
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id
    assert ndata.get('name') == "Janet Doe"


def test_delete_contact(app, token):
    client = app.test_client()
    result_add_contact = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_add_contact.status_code == 200
    data = json.loads(result_add_contact.data.decode())
    contact_id = data.get('id')
    assert contact_id is not None
    result = client.delete(
        '/api/contact/%d' % contact_id,
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id


def test_star_contact(app, token):
    client = app.test_client()
    result_add_contact = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_add_contact.status_code == 200
    data = json.loads(result_add_contact.data.decode())
    contact_id = data.get('id')
    assert contact_id is not None
    assert not data.get('starred')
    result = client.patch(
        '/api/contact/%d/star' % contact_id,
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id
    assert ndata.get('starred')


def test_unstar_contact(app, token):
    client = app.test_client()
    result_add_contact = client.post(
        "/api/contact",
        data=dict(
            name="Random Name",
            phonenumber="08000000000",
            email="remail@yahoo.com",
            address="#3 home",
        ),
        headers={"Authorization": "JWT %s" % token},
    )
    assert result_add_contact.status_code == 200
    data = json.loads(result_add_contact.data.decode())
    contact_id = data.get('id')
    assert contact_id is not None
    assert not data.get('starred')
    result = client.patch(
        '/api/contact/%d/star' % contact_id,
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id
    assert ndata.get('starred')
    result = client.patch(
        '/api/contact/%d/unstar' % contact_id,
        headers={"Authorization": "JWT %s" % token},
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert ndata.get('id') == contact_id
    assert not ndata.get('starred')


def test_read_all_starred_contacts(app, token):
    client = app.test_client()
    datas = [
        dict(
            name="Jane Dpe",
            phonenumber="08000000000",
            email="jad@yahoo.com",
            address="#3 home",
        ),
        dict(
            name="John Doe",
            phonenumber="08000000000",
            email="jod@yahoo.com",
            address="#3 home",
        ),
        dict(
            name="Johnny Depp",
            phonenumber="08000000000",
            email="jdp@yahoo.com",
            address="#3 home",
        ),
        dict(
            name="Mikail Hamza",
            phonenumber="08000000000",
            email="mh@yahoo.com",
            address="#3 home",
        ),
        dict(
            name="Salma Hayek",
            phonenumber="08000000000",
            email="sh@yahoo.com",
            address="#3 home",
        ),
    ]
    contact_ids = []
    for data in datas:
        result_add_contact = client.post(
            "/api/contact",
            data=data,
            headers={"Authorization": "JWT %s" % token},
        )
        assert result_add_contact.status_code == 200
        result_data = json.loads(result_add_contact.data.decode())
        contact_id = result_data.get('id')
        assert contact_id is not None
        contact_ids.append(contact_id)
    for index in range(3):
        result = client.patch(
            '/api/contact/%d/star' % contact_ids[index],
            headers={"Authorization": "JWT %s" % token},
        )
        assert result.status_code == 200
        ndata = json.loads(result.data.decode())
        assert ndata.get('id') == contact_ids[index]
        assert ndata.get('starred')
    result = client.get(
        '/api/contact/star', headers={"Authorization": "JWT %s" % token}
    )
    assert result.status_code == 200
    ndata = json.loads(result.data.decode())
    assert isinstance(ndata, list)
    assert len(ndata) == 3
