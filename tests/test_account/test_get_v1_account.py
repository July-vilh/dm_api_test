def test_get_v1_account(dm_api_facade):
    token = dm_api_facade.login.get_auth_token(login='login000015', password='login_000015')

    # print(token)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)
    dm_api_facade.account.current_user_info()

    # dm_api_facade.login.logout_user()
    # dm_api_facade.login.logout_user_all()
