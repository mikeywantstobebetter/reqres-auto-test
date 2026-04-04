import requests
import pytest
from api.login_api import register
import config
import allure


@allure.feature("注册模块")
class TestRegister:

    @allure.story("正常注册")
    def test_register_success(self, api_session):
        response = register(api_session, config.LOGIN_EMAIL, config.REGISTER_PASSWORD)
        assert response.status_code == 200
        assert response.json().get("id") is not None
        assert response.json().get("token") is not None


    @allure.story("无邮箱注册")
    @pytest.mark.parametrize("email", [None, ""])
    def test_register_no_email(self, api_session, email):
        response = register(api_session, email, config.LOGIN_PASSWORD)
        assert response.status_code == 400
        assert response.json().get("error") == "Missing email or username"

    @allure.story("无密码注册")
    @pytest.mark.parametrize("password", [None, ""])
    def test_register_no_password(self, api_session, password):
        response = register(api_session, config.LOGIN_EMAIL, password)
        assert response.status_code == 400
        assert response.json().get("error") == "Missing password"

    @allure.story("无API Key注册")
    def test_register_no_auth(self):
        json_data = {"email": "eve.holt@reqres.in", "password": "pistol1111"}
        response = requests.post(f"{config.BASE_URL}/api/register", json = json_data)
        assert response.status_code == 401
        assert response.json().get("error") == "missing_api_key"