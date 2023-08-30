# 2. Calling the user registration activation method (PUT)

def put_v1_account_token():
  import requests

  token = '221312'
  url = f"http://5.63.153.31:5051/v1/account/{token}"

  headers = {
    'X-Dm-Auth-Token': 'voluptate magna incididunt',
    'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="PUT",
    url=url,
    headers=headers
  )

  return response

