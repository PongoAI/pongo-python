import requests
from .utils import BASE_URL


def scrape_website(
    public_key,
    secret_key,
    sub_org_id,
    site_name,
    site_url,
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
    url = f"{BASE_URL}/api/{version}/scrape-website"

    payload = {"sub_org_id": sub_org_id, "url":site_url, "source": site_name}

    response = requests.post(url, headers=headers, json=payload)
    return response
