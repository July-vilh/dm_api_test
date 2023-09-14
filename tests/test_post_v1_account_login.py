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
        "login": "555559",
        "password": "login_221",
        "rememberMe": True
    }
    check_input_json_request(json)

    response = api.login.post_account_login(json=json)
    assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'


def check_input_json_request(json):
    for key, value in json.items():
        if key == "login":
            assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
        elif key == "password":
            assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
        elif key == "rememberMe":
            assert isinstance(value, bool), f'Value at the {key} should be bool, but now {type(value)}'
