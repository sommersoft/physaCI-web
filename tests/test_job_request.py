def test_request_valid_entry(client):
    node = 'dev-mocked-node-1'
    job_id = '11111111'
    url = f'/job?node={node}&job-id={job_id}'

    response = client.get(url)

    assert response.status_code < 400

def test_request_invalid_entry(client):
    node = 'dev-mocked-node-1'
    job_id = '1'
    url = f'/job?node={node}&job-id={job_id}'

    response = client.get(url)

    assert response.status_code == 404

def test_request_missing_param_node(client):
    job_id = '1'
    url = f'/job?job-id={job_id}'

    response = client.get(url)

    assert response.status_code == 400
    
def test_request_missing_param_jobid(client):
    node = 'dev-mocked-node-1'
    url = f'/job?node={node}'

    response = client.get(url)

    assert response.status_code == 400