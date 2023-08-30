# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run

def post_v1_account():
    import requests

    url = "http://5.63.153.31:5051/v1/account"

    payload = {
        "login": "login_8",
        "email": "login8@mail.ru",
        "password": "login_88"
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
        json=payload
    )

    return response


response = post_v1_account()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json)
