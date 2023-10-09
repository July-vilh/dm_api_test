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

    # для методов которые вместо параметров исп-ся авторизац. токен
    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        response = self.login_user(login=login, password=password, remember_me=remember_me)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return token

    def set_headers(self, headers):
        self.facade.login_api.client.session.update(headers)

    def logout_user(self, **kwargs):
        response = self.facade.login_api.delete_v1_account_login(**kwargs)
        return response

    def logout_user_all(self, **kwargs):
        response = self.facade.login_api.delete_v1_account_login_all(**kwargs)
        return response
