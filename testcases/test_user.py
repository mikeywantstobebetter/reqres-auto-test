import config
from api.user_api import *
import pytest
import allure

#pre-condition: 已经登录成功
@allure.feature("用户管理模块")
class TestUsers:
    @allure.story("获取所有用户成功")
    @pytest.mark.parametrize("page", [1,2])
    def test_get_users_success(self, api_session, page):
        response = get_users(api_session, page)
        assert response.status_code == 200
        assert response.json().get("page") == page
        assert response.json().get("data") is not None

    @allure.story("获取所有用户失败（无效页数)")
    def test_get_users_invalid_page(self, api_session):
        response = get_users(api_session, 999)
        assert response.status_code == 200
        assert response.json().get("data") == []

    
    #根据查询，user总共有12位
    @allure.story("获取单个用户成功")
    @pytest.mark.parametrize("user_id", [i for i in range(1 ,13)])
    def test_get_user_success(self, api_session, user_id):
        response = get_user(api_session, user_id)
        assert response.status_code == 200
        assert response.json().get("data")["id"] == user_id

    @allure.story("获取单个用户失败(无效用户ID)")
    def test_get_user_invalid_user_id(self, api_session):
        response = get_user(api_session, 999)
        assert response.status_code == 404


    #Reqres不校验user_id是否存在，update操作无论传入什么id都返回成功
    #因此只覆盖正向场景
    @allure.story("更新用户成功")
    @pytest.mark.parametrize("name, job", [("Mike", "tester"), ("John", "developer")])
    def test_update_user_success(self, api_session, name, job):
        response = update_user(api_session, 1, name, job)
        assert response.status_code == 200
        assert response.json().get("name") == name
        assert response.json().get("job") == job
        assert response.json().get("updatedAt") is not None



    #Reqres不校验user_id是否存在，且删除后数据仍然存在，只验证状态码
    @allure.story("删除用户成功(204 No Content)")
    def test_delete_user(self, api_session):
        response = delete_user(api_session, 1)
        assert response.status_code == 204