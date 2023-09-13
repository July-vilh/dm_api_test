import requests
from requests import Response

from ..models.registaration_model import Registrationmodel
from ..models.change_password import Change_password
from ..models.change_email import Change_email
from ..models.reset_password import Reset_password
from restclient1.restclient2 import restclient3
from dm_api_account.models.userenvelop import user_envelop


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = restclient3(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: Registrationmodel, **kwargs) -> Response:
        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def post_account_password_change(self, json: Registrationmodel, **kwargs) -> Response:
        response = self.client.post(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs):

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        user_envelop(**response.json())
        return response

    def put_account_email(self, json: Change_email, **kwargs) -> Response:
        response = self.client.put(
            path=f"/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def post_account_password_reset(self, json: Reset_password, **kwargs) -> Response:
        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        return response
