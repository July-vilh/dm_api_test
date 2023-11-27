# 3. Calling the method for authenticate via credentials (POST)
def test_post_v1_account_login(dm_api_facade):
    dm_api_facade.login.login_user(login="login000015", password="login_000015")
    # assert response.status_code == 200, f'Status code should be equal 200, but now status code {response.status_code}'


# def check_input_json_request(json):
#     for key, value in json.items():
#         if key == "login":
#             assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
#         elif key == "password":
#             assert isinstance(value, str), f'Value at the {key} should be str, but now {type(value)}'
#         elif key == "rememberMe":
#             assert isinstance(value, bool), f'Value at the {key} should be bool, but now {type(value)}'
