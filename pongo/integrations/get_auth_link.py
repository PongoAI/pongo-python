import time
from typing import List
import requests
from ..utils import BASE_URL


def get_auth_link(
    secret_key,
    sub_org_id,
    integration_name,
    redirect_uri,
    version="v1",
):
    """
    Generates a link that sub-organizations can use to authenticate with other platforms and have their data ingested by Pongo.

    :param id: ID of the sub-organization to generate a link for
    :param integration_name: Name of the integration to authenticate with
    :param redirect_uri: The address users will be sent to after completing the authentication process- wether successful or unsuccessful.
    :return: Response from the server containing the authentication link or error message.
    """

    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-org/auth-link?sub_org_id={sub_org_id}&integration_name={integration_name}&redirect_uri={redirect_uri}"

    response = requests.get(url, headers=headers)
    return response
