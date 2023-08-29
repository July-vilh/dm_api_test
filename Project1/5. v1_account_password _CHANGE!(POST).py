# 5. Calling method for change password (POST)

import requests
import json

url = "http://5.63.153.31:5051/v1/account/password"

payload = json.dumps({
  "login": "login_6",
  "token": "2d9eead9-2a3f-4e58-8865-cea4d363e4eb",
  "oldPassword": "login_66",
  "newPassword": "login_67"
})
headers = {
  'X-Dm-Auth-Token': 'voluptate magna incididunt',
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
