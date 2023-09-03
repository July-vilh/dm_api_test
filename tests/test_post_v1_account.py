# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run

from Services.dm_api_account import dmapiaccount
from Services.mailhog import mailhog_api
def test_post_v1_account():
    mailhog = mailhog_api(host='http://5.63.153.31:5025')
    api = dmapiaccount(host='http://5.63.153.31:5051')


    json = {
        "login": "login_33",
        "email": "login33@mail.ru",
        "password": "login_33"
    }
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    print(response)
    print(response.json())

