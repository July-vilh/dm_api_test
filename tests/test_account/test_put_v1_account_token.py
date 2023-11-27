# 2. Calling the user registration activation method (PUT)

# import json
from hamcrest import assert_that, has_properties
from Services.dm_api_account import Facade
from generic.helpers.mailhog import mailhog_api
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = mailhog_api(host='http://5.63.153.31:5025/')
    api = Facade(host=f'http://5.63.153.31:5051')

    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

    assert_that(response.resource, has_properties(
        {
            "login": "login0001"
        }
    ))



    # expected_json = {"resource": {
    #     "login": "login00012",
    #     "rating": {
    #         "enabled": True,
    #         "quality": 0,
    #         "quantity": 0
    #     },
    #     "roles": [
    #         "Guest",
    #         "Player"
    #     ]
    # }
    # }
    #
    # actual_json = json.loads(response.json(by_alias=True, exclude_none=True))
    # assert actual_json==expected_json
