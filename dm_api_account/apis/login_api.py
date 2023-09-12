import requests
from requests import Response
from ..models.login_credentials import Login_credentials
from restclient1.restclient2 import restclient3


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = restclient3(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_account_login(self, json: Login_credentials, **kwargs) -> Response:
        response = self.client.post(
            path=f"/v1/account/login",
            json=json,
            **kwargs
        )
        return response
