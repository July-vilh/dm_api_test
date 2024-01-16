import allure
from dm_api_account.models import *


class Login:
    def __init__(self, facade):
        from Services.dm_api_account import Facade
        self.facade: Facade = facade

    def login_user(self, login: str, password: str, remember_me: bool = True):
        with allure.step("Log in user"):
            response = self.facade.login_api.v1_account_login_post(
                login_credentials=LoginCredentials(
                    login=login,
                    password=password,
                    remember_me=remember_me
                ),
                # ожидаемый статус код:
                status_code=200
            )
        return response

    # для методов которые вместо параметров исп-ся авторизац. токен
    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        response = self.login_user(login=login, password=password, remember_me=remember_me)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return token

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def logout_user(self, **kwargs):
        response = self.facade.login_api.v1_account_login_delete(**kwargs)
        return response

    def logout_user_all(self, **kwargs):
        response = self.facade.login_api.v1_account_login_all_delete(**kwargs)
        return response
