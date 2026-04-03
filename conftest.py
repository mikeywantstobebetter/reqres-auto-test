import pytest
import requests
import config
from api.login_api import login


@pytest.fixture(scope = "session")
def auth_session():
    session = requests.Session()
    session.headers.update({
        "x-api-key": config.API_KEY
    })

    #拿token
    response = login(session, config.LOGIN_EMAIL, config.LOGIN_PASSWORD)
    token = response.json().get("token")
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session