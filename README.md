# Reqres 接口自动化测试框架

## 项目简介

基于 Python + pytest + requests 搭建的接口自动化测试框架，对 [Reqres](https://reqres.in) 平台的登录、注册、用户管理等接口进行自动化测试，集成 Allure 生成可视化测试报告。

## 技术栈

- Python 3.x
- pytest
- requests
- allure-pytest

## 项目结构

```
reqres-auto-test/
├── api/                  # 接口封装层
│   ├── login_api.py      # 登录、注册接口
│   └── user_api.py       # 用户管理接口
├── testcases/            # 测试用例层
│   ├── test_login.py     # 登录模块测试
│   ├── test_register.py  # 注册模块测试
│   └── test_user.py      # 用户管理模块测试
├── conftest.py           # pytest全局fixture（session管理）
├── config_example.py     # 配置文件模板
└── pytest.ini            # pytest配置
```

## 测试覆盖范围

| 模块 | 用例数 | 覆盖场景 |
|------|--------|---------|
| 登录模块 | 6 | 正常登录、无API Key、缺少邮箱、缺少密码 |
| 注册模块 | 6 | 正常注册、无API Key、缺少邮箱、缺少密码 |
| 用户管理模块 | 19 | 获取列表、获取单个用户、更新用户、删除用户 |

## 如何运行

1. 克隆项目

```bash
git clone https://github.com/mikeywantstobebetter/reqres-auto-test.git
cd reqres-auto-test
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置环境

```bash
cp config_example.py config.py
# 编辑 config.py，填入你的 API Key
```

4. 运行测试

```bash
pytest
```

5. 查看报告

```bash
allure serve reports/allure-results
```

## 框架设计

- **分层设计**：api层负责接口封装，testcases层负责测试逻辑，职责清晰
- **session统一管理**：通过conftest.py集中管理请求session和鉴权信息
- **数据驱动**：使用pytest.mark.parametrize实现参数化测试
- **可视化报告**：集成allure，按功能模块分类展示测试结果
