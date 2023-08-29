# 4. Calling the method for authenticate via credentials (POST)

import requests
import json

url = "http://5.63.153.31:5051/v1/account/login"

payload = json.dumps({
  "login": "login_6",
  "password": "login_66",
  "rememberMe": True
})
headers = {
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
