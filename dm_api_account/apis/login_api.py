import requests
from requests import Response
from ..models.login_credentials import Login_credentials
from requests import session

class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers.update(headers) if headers else None


    def post_account_login(self, json: Login_credentials, **kwargs) -> Response:

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response
