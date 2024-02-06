import time
from typing import List
import requests
from ..utils import BASE_URL


def update_drive_directories(
    secret_key,
    new_dirs,
    integration_id,
    version="v1",
):
    """
    Generates a link that sub-organizations can use to authenticate with other platforms and have their data ingested by Pongo.

    :param integration_id: ID of the google drive integration to update
    :param new_dirs: Array containing the new "enabled" states of google drive directories, id's and length must be the same
    :param redirect_uri: The address users will be sent to after completing the authentication process- wether successful or unsuccessful.
    :return: Response from the server containing the authentication link or error message.
    """

    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/google-drive/update-dirs"

    response = requests.post(
        url,
        headers=headers,
        json={"new_dirs": new_dirs, "integration_id": integration_id},
    )
    return response
