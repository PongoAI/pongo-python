import time
import uuid
import requests
import os
import base64
from .utils import BASE_URL

MAX_FILE_SIZE = 20 * 1024 * 1024


def upload(
    public_key,
    secret_key,
    sub_org_id,
    source_name,
    data,
    metadata={},
    parent_id=None,
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
    url = f"{BASE_URL}/api/{version}/upload-data"

    if type(data) == str or type(data) == list:
        payload = {
            "sub_org_id": sub_org_id,
            "source": source_name,
            "data": data,
            "metadata": metadata,
            "timestamp": timestamp,
            "parent_id": parent_id,
        }

    if not timestamp:
        payload["timestamp"] = int(time.time())

    if not parent_id:
        payload["parent_id"] = str(uuid.uuid4())

    response = requests.post(url, headers=headers, json=payload)
    return response


def upload_pdf(
    public_key,
    secret_key,
    sub_org_id,
    source_name,
    file_path,
    metadata={},
    parent_id=None,
    timestamp=None,
    version="v1",
):
    """
    Uploads a file to a specified URL using provided credentials.
    """

    headers = {
        "secret": secret_key,
        "id": public_key,
    }
    url = f"{BASE_URL}/api/{version}/upload-pdf"

    payload = {
        "sub_org_id": sub_org_id,
        "source": source_name,
        "metadata": metadata,
        "timestamp": timestamp,
        "parent_id": parent_id,
    }

    if not timestamp:
        payload["timestamp"] = int(time.time())

    if not parent_id:
        payload["parent_id"] = str(uuid.uuid4())

    if file_path.endswith(".pdf"):
        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE:
            raise ValueError(
                "The file is too large. Please provide a file that is less than 20MB."
            )

        file_name = os.path.basename(file_path)

        files = [("file", (file_name, open(file_path, "rb"), "application/pdf"))]
        return requests.request("POST", url, headers=headers, data=payload, files=files)
    else:
        raise ValueError("Provided file is not a PDF.")
