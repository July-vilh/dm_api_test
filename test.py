import requests
import json

url = "http://5.63.153.31:5051/v1/account"

payload = json.dumps({
  "login": "login_6",
  "email": "login6@mail.ru",
  "password": "login_66"
})
headers = {
  'X-Dm-Auth-Token': 'voluptate magna incididunt',
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
