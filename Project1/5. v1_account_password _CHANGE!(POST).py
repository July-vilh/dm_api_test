# 5. Calling method for change password (POST)

def post_account_password_chande():
  import requests

  url = "http://5.63.153.31:5051/v1/account/password"

  payload = {
    "login": "login_6",
    "token": "2d9eead9-2a3f-4e58-8865-cea4d363e4eb",
    "oldPassword": "login_66",
    "newPassword": "login_67"
  }
  headers = {
    'X-Dm-Auth-Token': 'voluptate magna incididunt',
    'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="PUT",
    url=url,
    headers=headers,
    json=payload
  )

  return response


response = post_account_password_chande()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json)
