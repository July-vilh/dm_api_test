# from apis.dm_api_account import Registration
from apis.dm_api_account.models import *
try:
    from Services.dm_api_account import Facade
except ImportError:
    ...


class Account:
    def __init__(self, facade: Facade):
        self.facade = facade

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(token=token)
        return response

    def current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)



