# 2. Calling the user registration activation method (PUT)

import requests

url = "http://5.63.153.31:5051/v1/account/4b06f182-322c-4ded-bcde-9de97f41f4ea"

payload = ""
headers = {
  'X-Dm-Auth-Token': 'voluptate magna incididunt',
  'X-Dm-Bb-Render-Mode': 'voluptate magna incididunt',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
