from Services.dm_api_account import Facade

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    token = api.login.get_auth_token(login='login00336', password='login_00336')
    # print(token)
    api.account.set_headers(headers=token)
    api.login_api.set_headers(headers=token)

    api.account_api.current_user_info()
    api.login.logout_user()
    api.login.logout_user_all()
