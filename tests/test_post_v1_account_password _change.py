# 5. Calling method for change password (POST)

from Services.dm_api_account import dmapiaccount
from generic.helpers.mailhog import mailhog_api
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
        "login": 555559,
        "oldPassword": "login_221",
        "newPassword": "login_222"
    }

    # response = api.account.post_account_password_change(json=create_password_json)
    # assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'

    check_input_json_request(json)

    token = mailhog.get_token_from_last_email()
    update_password_json = {
        "token": token
    }
    response = api.account.post_account_password_change(json=update_password_json)
    assert response.status_code == 200, f'Status code should be equal 201, but now status code {response.status_code}'


def check_input_json_request(json):
    for key, value in json.items():
        if key == "login":
            assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
        elif key == "oldPassword":
            assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
        elif key == "newPassword":
            assert isinstance(value, str), f'Value at the {key} should be bool, but now {type(value)}'
