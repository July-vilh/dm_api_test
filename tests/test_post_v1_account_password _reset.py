# 6. Calling method for RESET registered password (POST)

from Services.dm_api_account import dmapiaccount
def test_post_v1_account_password_reset():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
    "login": "login_20",
    "email": "login20@mail.ru"
    }
    response = api.account.post_account_password_reset(
        json=json
    )
    print(response)
