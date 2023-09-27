from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, facade):
        self.facade = facade

    def login_user(self, login: str, password: str, remember_me: bool = True):
        response = self.facade.login_api.post_account_login(
            json=LoginCredentials(
                login=login,
                password=password,
                rememberMe=remember_me
            ),
            # ожидаемый статус код:
            status_code=200
        )
        return response
