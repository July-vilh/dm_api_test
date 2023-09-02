# 3. Calling the method for authenticate via credentials (POST)

from Services.dm_api_account import dmapiaccount
def test_post_v1_account_login():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
    "login": "login_20",
    "password": "login_20",
    "rememberMe": True
    }
    response = api.login.post_account_login(
        json=json
    )
    print(response)
