# 6. Calling method GET Currect user (GET)

import requests

url = "http://5.63.153.31:5051/v1/account"

payload = ""
headers = {
  'X-Dm-Auth-Token': 'voluptate magna incididunt',
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
