import requests
import pytest
from api.login_api import register
import config



def test_register_success(api_session):
    response = register(api_session, config.LOGIN_EMAIL, config.LOGIN_PASSWORD)
    assert response.status_code == 200
    assert response.json().get("id") is not None
    assert response.json().get("token") is not None

@pytest.mark.parametrize("email", [None, ""])
def test_register_no_email(api_session, email):
    response = register(api_session, email, config.LOGIN_PASSWORD)
    assert response.status_code == 400
    assert response.json().get("error") == "Missing email or username"

@pytest.mark.parametrize("password", [None, ""])
def test_register_no_password(api_session, password):
    response = register(api_session, config.LOGIN_EMAIL, password)
    assert response.status_code == 400
    assert response.json().get("error") == "Missing password"

def test_register_no_auth():
    json_data = {"email": "eve.holt@reqres.in", "password": "pistol1111"}
    response = requests.post(f"{config.BASE_URL}/api/register", json = json_data)
    assert response.status_code == 401
    assert response.json().get("error") == "missing_api_key"