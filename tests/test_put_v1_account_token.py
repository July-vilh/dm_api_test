# 2. Calling the user registration activation method (PUT)

from Services.dm_api_account import dmapiaccount
from Services.mailhog import mailhog_api
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = mailhog_api(host='http://5.63.153.31:5025/')
    api = dmapiaccount(host=f'http://5.63.153.31:5051')

    # response = api.account.put_v1_account_token(token=token)
    # print(response)

    # response = api.account.put_v1_account_token(token=None, json=None)
    # assert response.status_code == 201, f'Status code should be equal 201, but now status code {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
