import os
import sys

import pytest

import application

@pytest.fixture
def client(monkeypatch):
    if not os.environ.get('PHYSACI_JOB_RESULT_URL'):
        monkeypatch.setenv('PHYSACI_JOB_RESULT_URL', 'https://physaci-app.azurewebsites.net/api/job-result')

    application.app.config['TESTING'] = True

    with application.app.test_client() as client:
        yield client

    monkeypatch.delenv('PHYSACI_JOB_RESULT_URL', raising=False)    
