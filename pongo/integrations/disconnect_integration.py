import time
from typing import List
import requests
from ..utils import BASE_URL


def disconnect_integration(
    secret_key,
    integration_id,
    integration_name,
    version="v1",
):
    """
    Disconnect an integration and delete all of its data

    :param id: ID of the integration to delete
    :param name: Name of the integration to delete
    :return: Response from the server which may contain a disconnect link for the end user, depending on the integration.
    """

    headers = {
        "secret": secret_key,
    }

    url = f"{BASE_URL}/api/{version}/org/disconnect-integration"

    response = requests.post(
        url,
        headers=headers,
        json={"integration_id": integration_id, "integration_name": integration_name},
    )
    return response
