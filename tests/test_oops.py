def test_oops(client):
    url = f'/fake-path'

    response = client.get(url)

    assert response.status_code == 404