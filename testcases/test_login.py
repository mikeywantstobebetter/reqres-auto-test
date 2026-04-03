import config
from api.login_api import login
import requests
import pytest

def test_login_success(api_session):
    response = login(api_session, config.LOGIN_EMAIL, config.LOGIN_PASSWORD)
    assert response.status_code == 200
    assert response.json().get("token") is not None


def test_login_no_auth():
    json_data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    response = requests.post(f"{config.BASE_URL}/api/login", json = json_data)
    assert response.status_code == 401
    assert response.json().get("error") == "missing_api_key"

@pytest.mark.parametrize("password", [None, ""])
def test_login_no_password(api_session, password):
    response = login(api_session, config.LOGIN_EMAIL, password)
    assert response.status_code == 400
    assert response.json().get("error") == "Missing password"


@pytest.mark.parametrize("email", [None, ""])
def test_login_no_email(api_session, email):
    response = login(api_session, email, config.LOGIN_PASSWORD)
    assert response.status_code == 400
    assert response.json().get("error") == "Missing email or username"