import requests
from .utils import BASE_URL


def create_sub_org(
    secret_key,
    sub_org_name,
    version="v1",
):
    """
    Creates a sub org, with a given name, returns the sub org id and metadata.
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-org"

    payload = {
        "sub_org_name": sub_org_name,
    }

    response = requests.post(url, headers=headers, json=payload)
    return response


def get_sub_orgs(
    secret_key,
    version="v1",
):
    """
    Returns list of all sub orgs.
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-orgs"

    response = requests.get(url, headers=headers)
    return response


def get_sub_org(
    secret_key,
    sub_org_id,
    version="v1",
):
    """
    Retrieves a sub org by ID
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-org"

    payload = {
        "sub_org_id": sub_org_id,
    }

    params = {
        key: value if not isinstance(value, list) else ",".join(value)
        for key, value in payload.items()
        if value is not None
    }
    response = requests.get(url, headers=headers, params=params)
    return response


def delete_sub_org(
    secret_key,
    sub_org_id,
    version="v1",
):
    """
    Delete a sub org by ID.
    Will also delete all data associated with the sub org.
    BE CAREFUL USING THIS METHOD!
    """

    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-org"

    payload = {
        "sub_org_id": sub_org_id,
    }

    params = {
        key: value if not isinstance(value, list) else ",".join(value)
        for key, value in payload.items()
        if value is not None
    }
    response = requests.delete(url, headers=headers, params=params, timeout=120)
    return response


def update_sub_org(
    secret_key,
    sub_org_id,
    sub_org_name,
    version="v1",
):
    """
    Update a sub-organization's name
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/sub-org"

    payload = {"sub_org_id": sub_org_id, "sub_org_name": sub_org_name}

    params = {
        key: value if not isinstance(value, list) else ",".join(value)
        for key, value in payload.items()
        if value is not None
    }
    response = requests.put(url, headers=headers, json=params)
    return response
