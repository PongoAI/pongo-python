import requests
from .utils import BASE_URL


def search(
    secret_key,
    query,
    sub_org_id=None,
    num_results=10,
    sample_size=15,
    reduce_tokens=False,
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
    }
    url = f"{BASE_URL}/api/{version}/search"

    payload = {
        "sub_org_id": sub_org_id,
        "query": query,
        "sources": sources,
        "start_time": start_time,
        "end_time": end_time,
        "reduce_tokens": reduce_tokens,
        "num_results": num_results,
        "sample_size": sample_size,
    }

    params = {
        key: value if not isinstance(value, list) else ",".join(value)
        for key, value in payload.items()
        if value is not None
    }
    response = requests.get(url, headers=headers, params=params)
    return response
