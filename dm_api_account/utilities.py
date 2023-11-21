import requests


def validate_request_json(json):
    if isinstance(json, dict):
        return json
    return json.dict(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code, f'Status code should be equal {status_code}, but now status code {response.status_code} '
