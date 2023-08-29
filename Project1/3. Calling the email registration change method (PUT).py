# 3. Calling the email registration change method (PUT)

import requests
import json

url = "http://5.63.153.31:5051/v1/account/email"

payload = json.dumps({
  "login": "login_6",
  "password": "login_66",
  "email": "login7@mail.ru"
})
headers = {
  'X-Dm-Auth-Token': 'voluptate magna incididunt',
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

# after go the e-mail with new token -> add this token and run POST method (registration user)!!!!!
