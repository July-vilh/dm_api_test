# 4. Calling the email registration change method (PUT)

from Services.dm_api_account import dmapiaccount
from Services.mailhog import mailhog_api
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = mailhog_api(host='http://5.63.153.31:5025/')
    api = dmapiaccount(host='http://5.63.153.31:5051')
    create_user_json = {
        "login": "login_20",
        "password": "login_20",
        "email": "login20@mail.ru"
    }
    response = api.account.put_account_email(json=create_user_json)
    assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'

    token = mailhog.get_token_from_last_email()

# after go the e-mail with new token -> add this token and run POST method (through the enter new token at the
    # Activate registered user (POST)))!!!!!

    update_email_json = {
        "token": token
    }
    response = api.account.put_account_email(json=update_email_json)
    assert response.status_code == 200, f'Status code should be equal 201, but now status code {response.status_code}'

