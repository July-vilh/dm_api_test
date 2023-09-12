# 3. Calling the method for authenticate via credentials (POST)

from Services.dm_api_account import dmapiaccount
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
        "login": "login_5677",
        "password": "login_5677",
        "rememberMe": True
    }

    response = api.login.post_account_login(json=json)
    assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
