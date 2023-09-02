# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run

from Services.dm_api_account import dmapiaccount
def test_post_v1_account():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
    "login": "login_20",
    "email": "login20@mail.ru",
    "password": "login_20"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)

