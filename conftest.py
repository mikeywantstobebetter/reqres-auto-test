import pytest
import requests
import config
from api.login_api import login


@pytest.fixture(scope = "session")
def api_session():
    session = requests.Session()
    session.headers.update({
        "x-api-key": config.API_KEY
    })
    return session


@pytest.fixture(scope = "session")
def auth_session(api_session):
    response = login(api_session, config.LOGIN_EMAIL, config.LOGIN_PASSWORD)
    token = response.json().get("token")
    api_session.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return api_session

    