def test_root_path(client):
    url = '/'

    response = client.get(url)

    assert response.status_code < 300