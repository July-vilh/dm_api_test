# 5. Calling method for change password (POST)

from Services.dm_api_account import dmapiaccount
from Services.mailhog import mailhog_api
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = mailhog_api(host='http://5.63.153.31:5025/')
    api = dmapiaccount(host='http://5.63.153.31:5051')
    create_password_json = {
        "login": "login_5677",
        "oldPassword": "login_5677",
        "newPassword": "login_666"
    }

    response = api.account.post_account_password_change(json=create_password_json)
    assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'

    token = mailhog.get_token_from_last_email()
    update_password_json = {
        "token": token
    }
    response = api.account.post_account_password_change(json=update_password_json)
    assert response.status_code == 200, f'Status code should be equal 201, but now status code {response.status_code}'
