import json
from requests import session, Response
import pprint
from restclient1.restclient2 import restclient3


class mailhog_api:
    def __init__(self, host='http://5.63.153.31:5025/'):
        self.host = host
        self.client = restclient3(host=host)

    def get_api_v2_messages(self, limit: int = 50) -> Response:
        response = self.client.get(
            path=f"api/v2/messages",
            params={
                limit: 'limit'
            }
        )

        return response

    def get_token_from_last_email(self) -> str:
        emails = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]
        return token


response = mailhog_api().get_api_v2_messages(limit=50)
pprint.pprint(response.json())
