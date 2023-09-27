import requests
from requests import Response
from model import *
from restclient1.restclient2 import restclient3
from dm_api_account.utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = restclient3(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_account_login(self, json: LoginCredentials, status_code: int, **kwargs) -> Response:
        response = self.client.post(
            path=f"/v1/account/login",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        return response
