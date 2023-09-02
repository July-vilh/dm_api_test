# 2. Calling the user registration activation method (PUT)

from Services.dm_api_account import dmapiaccount
def test_put_v1_account_token():
  api = dmapiaccount(host=f'http://5.63.153.31:5051')

  response = api.account.put_v1_account_token()
  print(response)
