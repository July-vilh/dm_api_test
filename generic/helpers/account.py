# from apis.dm_api_account import Registration
from dm_api_account.models import *

class Account:
    def __init__(self, facade):
        from Services.dm_api_account import Facade
        self.facade: Facade = facade

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.register(
            registration=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.activate(token=token)
        return response

    def current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)



