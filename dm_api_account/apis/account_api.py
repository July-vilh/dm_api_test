import requests
from requests import Response
from ..models.registaration_model import Registration_model
from ..models.change_password import Change_password
from ..models.change_email import Change_email
from ..models.reset_password import Reset_password
from requests import session
class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: Registration_model, **kwargs) -> Response:

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_account_password_change(self, json: Change_password, **kwargs) -> Response:

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self):

        token = 'd7a59f9f-a77c-4ed9-9735-8567166b4e48'
        response = requests.put(
            url=f"{self.host}/v1/account/{token}"
        )
        return response

    def put_account_email(self, json: Change_email, **kwargs) -> Response:

        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def post_account_password_reset(self, json: Reset_password, **kwargs) -> Response:

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response
