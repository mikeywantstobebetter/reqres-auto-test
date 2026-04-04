import config
from api.login_api import login
import requests
import pytest
import allure

@allure.feature("登录模块")
class TestLogin:

    @allure.story("正常登录")
    def test_login_success(self, api_session):
        response = login(api_session, config.LOGIN_EMAIL, config.LOGIN_PASSWORD)
        assert response.status_code == 200
        assert response.json().get("token") is not None

    @allure.story("无API Key登录")
    def test_login_no_auth(self):
        json_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
        }
        response = requests.post(f"{config.BASE_URL}/api/login", json = json_data)
        assert response.status_code == 401
        assert response.json().get("error") == "missing_api_key"

    @allure.story("无密码登录")
    @pytest.mark.parametrize("password", [None, ""])
    def test_login_no_password(self, api_session, password):
        response = login(api_session, config.LOGIN_EMAIL, password)
        assert response.status_code == 400
        assert response.json().get("error") == "Missing password"

    @allure.story("无邮箱登录")
    @pytest.mark.parametrize("email", [None, ""])
    def test_login_no_email(self, api_session, email):
        response = login(api_session, email, config.LOGIN_PASSWORD)
        assert response.status_code == 400
        assert response.json().get("error") == "Missing email or username"