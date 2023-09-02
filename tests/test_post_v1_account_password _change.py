# 5. Calling method for change password (POST)

from Services.dm_api_account import dmapiaccount
def test_post_v1_account():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
    "login": "login_20",
    "token": "d7a59f9f-a77c-4ed9-9735-8567166b4e48",
    "oldPassword": "login_20",
    "newPassword": "login_666"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
