import time
import uuid
import requests
import os
import base64
from .utils import BASE_URL

MAX_FILE_SIZE = 20 * 1024 * 1024


def upload(
    secret_key,
    data,
    sub_org_id=None,
    metadata={},
    timestamp=None,
    version="v1",
):
    """
    Uploads data to pongo and returns a job id for the upload.

    :param file_path: Path to the file to be uploaded.
    :param destination_url: URL where the file will be uploaded.
    :param creds: Credentials used for authentication.
    :return: Response from the server.
    """

    headers = {
        "secret": secret_key,
    }
    payload = {}
    url = f"{BASE_URL}/api/{version}/upload-data"

    if type(data) == str or type(data) == list:
        payload = {
            "sub_org_id": sub_org_id,
            "data": data,
            "metadata": metadata,
            "timestamp": timestamp,
        }
    else:
        raise ValueError("Data must be a string or a list of strings.")

    if type(metadata) == dict:
        if "parent_id" not in metadata:
            raise ValueError("Metadata must contain a parent_id.")

        if "source" not in metadata:
            raise ValueError("Metadata must contain a source.")

    elif type(metadata) == list:
        for indx, meta in enumerate(metadata):
            if "parent_id" not in meta:
                raise ValueError(
                    f"Metadata must contain a parent_id. Missing at index {indx}."
                )

            if "source" not in meta:
                raise ValueError(
                    f"Metadata must contain a source. Missing at index {indx}."
                )
    else:
        raise ValueError("Metadata must be a dictionary or a list of dictionaries.")

    if not timestamp:
        payload["timestamp"] = int(time.time())

    response = requests.post(url, headers=headers, json=payload)
    return response


def upload_pdf(
    secret_key,
    source_name,
    file_path,
    sub_org_id=None,
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
        with open(file_path, "rb") as pdf_file:
            files = [("file", (file_name, pdf_file, "application/pdf"))]
            response = requests.request(
                "POST", url, headers=headers, data=payload, files=files
            )
        return response
    else:
        raise ValueError("Provided file is not a PDF.")
