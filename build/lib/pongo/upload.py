import time
from typing import List
import requests
from .utils import BASE_URL


def upload(
    public_key,
    secret_key,
    sub_org,
    source_name,
    data,
    metadata={},
    timestamp=None,
    version="v1",
):
    """
    Uploads a file to a specified URL using provided credentials.

    :param file_path: Path to the file to be uploaded.
    :param destination_url: URL where the file will be uploaded.
    :param creds: Credentials used for authentication.
    :return: Response from the server.
    """

    headers = {
        "secret": secret_key,
        "id": public_key,
    }
    payload = {}
    url = f"{BASE_URL}/api/{version}/upload_data"

    
    if type(data) == str or type(data) == list:
        payload = {
            "sub_org_id": sub_org,
            "source_name": source_name,
            "data": data,
            "metadata": metadata,
        }


    if not timestamp:
        payload["timestamp"] = int(time.time())

    response = requests.post(url, headers=headers, json=payload)
    return response
