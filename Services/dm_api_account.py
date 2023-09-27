from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from generic.helpers.account import Account
from generic.helpers.login import Login
from generic.helpers.mailhog import mailhog_api


class Facade:
    def __init__(self, host, mailhog_host = None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = mailhog_api()
        self.account = Account(self)
        self.login = Login(self)