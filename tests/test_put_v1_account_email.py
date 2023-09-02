# 4. Calling the email registration change method (PUT)

from Services.dm_api_account import dmapiaccount
def test_put_v1_account_email():
    api = dmapiaccount(host='http://5.63.153.31:5051')
    json = {
    "login": "login_20",
    "password": "login_20",
    "email": "login20@mail.ru"
    }
    response = api.account.put_account_email(
        json=json
    )
    print(response)

# after go the e-mail with new token -> add this token and run POST method (through the enter new token at the Activate registered user (POST)))!!!!!
