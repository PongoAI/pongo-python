import requests
from .utils import BASE_URL


def get(
    secret_key,
    sub_org_id=None,
    doc_id=None,
    parent_id=None,
    version="v1",
):
    """
    Retrieves a single document chunk or a list of document chunks from the Pongo API.
    :param doc_id: ID of the document to be retrieved.
    :param parent_id: ID of the parent document to be retrieved. Will return all chunks of the parent document.
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/data"

    if not doc_id and not parent_id:
        raise Exception("Must provide either doc_id or parent_id")

    if doc_id and parent_id:
        raise Exception("Cannot provide both doc_id and parent_id")

    payload = {
        "sub_org_id": sub_org_id,
        "doc_id": doc_id,
        "parent_id": parent_id,
    }

    params = {
        key: value if not isinstance(value, list) else ",".join(value)
        for key, value in payload.items()
        if value is not None
    }
    response = requests.get(url, headers=headers, params=params)
    return response
