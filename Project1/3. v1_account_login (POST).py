# 3. Calling the method for authenticate via credentials (POST)

def post_account_login():
  import requests

  url = "http://5.63.153.31:5051/v1/account/login"

  payload = {
    "login": "login_6",
    "password": "login_66",
    "rememberMe": True
  }
  headers = {
    'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="POST",
    url=url,
    headers=headers,
    json=payload
  )

  return response


response = post_account_login()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json)
