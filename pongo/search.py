import requests
from .utils import BASE_URL


def search(
    public_key,
    secret_key,
    sub_org_id,
    query,
    num_results=15,
    max_reranker_results=5,
    start_time=None,
    end_time=None,
    sources=[],
    version="v1",
):
    """
    Searches for data in the Pongo API.
    OPTIONAL: start_time, end_time, sources
    """
    headers = {
        "secret": secret_key,
        "id": public_key,
    }
    url = f"{BASE_URL}/api/{version}/search"

    payload = {
        "sub_org_id": sub_org_id,
        "query": query,
        "sources": sources,
        "start_time": start_time,
        "end_time": end_time,
        "num_results": num_results,
        "max_reranker_results": max_reranker_results,
    }

    params = {key: value if not isinstance(value, list) else ','.join(value) for key, value in payload.items() if value is not None}
    response = requests.get(url, headers=headers, params=params)
    return response
