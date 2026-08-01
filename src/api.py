import requests

from config import (
    APP_ID,
    APP_SECRET,
    SID,
    BASE_URL,
)


from auth import build_headers


def get_system_details():
    """Vraag systeemgegevens op bij APsystems."""

    request_path = f"/user/api/v2/systems/details/{SID}"

    signature_path = request_path.rsplit("/", 1)[1]

    headers = build_headers(
        APP_ID,
        APP_SECRET,
        signature_path,
)

    url = BASE_URL + request_path


    response = requests.get(
        url,
        headers = headers,
    )

    print("HTTP status:", response.status_code)
    print("Response:")
    print(response.text)

    return response.json()