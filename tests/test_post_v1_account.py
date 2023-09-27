# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run

from Services.dm_api_account import dmapiaccount
from Services.mailhog import mailhog_api
import structlog
from dm_api_account.models.registaration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = mailhog_api(host='http://5.63.153.31:5025/')
    api = dmapiaccount(host='http://5.63.153.31:5051')

    json = Registration(
        login="login0001",
        email="login2256@mail.ru",
        password="login_2256"
    )
    response = api.account.post_v1_account(json=json)

    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

# def check_input_json_request(json):
#     for key, value in json.tems():
#         if key == "login":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "email":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "password":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
