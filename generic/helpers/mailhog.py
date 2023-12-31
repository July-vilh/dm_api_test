import json
import time

from requests import Response
# import pprint
from common_libs.restclient1.restclient2 import restclient3


def decorator(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 1:
                print(f'attempt {i}')
                time.sleep(2)
                continue
            else:
                return response

    return wrapper


class mailhog_api:
    def __init__(self, host='http://5.63.153.31:5025/'):
        self.host = host
        self.client = restclient3(host=host)

    # @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        response = self.client.get(
            path=f"api/v2/messages",
            params={
                limit: 'limit'
            }
        )

        return response

    def get_token_from_last_email(self) -> str:
        time.sleep(2)
        emails = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]
        return token

    def get_token_by_login(self, login: str, attempt=50):
        if attempt == 0:
            raise AssertionError(f'the mails don-t get with login {login}')
        emails = self.get_api_v2_messages(limit=100).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                return token
        time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def delete_all_messages(self):
        response = self.client.delete(path='api/v1/messages')
        return response



# response = mailhog_api().get_api_v2_messages(limit=50)
# pprint.pprint(response.json())
