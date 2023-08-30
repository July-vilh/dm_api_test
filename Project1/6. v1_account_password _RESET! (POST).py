# 6. Calling method for RESET registered password (POST)

def post_account_password_reset():
  import requests

  url = "http://5.63.153.31:5051/v1/account/password"

  payload = {
    "login": "login_6",
    "email": "login7@mail.ru"
  }
  headers = {
    'X-Dm-Auth-Token': 'voluptate magna incididunt',
    'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="POST",
    url=url,
    headers=headers,
    data=payload
  )

  return response


response = post_account_password_reset()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json)
