# 4. Calling the email registration change method (PUT)

def put_account_email():
  import requests

  url = "http://5.63.153.31:5051/v1/account/email"

  payload = {
    "login": "login_6",
    "password": "login_66",
    "email": "login7@mail.ru"
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


response = put_account_email()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json)

# after go the e-mail with new token -> add this token and run POST method (through the enter new token at the Activate registered user (POST)))!!!!!
