import requests
import json


def test():
    url = "https://api.omicsanalytics.com/api/auth/login"

    payload = json.dumps({
        "email": None,
        "password": "password"  # insert password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    return response.status_code == 400


if __name__ == "__main__":
    test()
