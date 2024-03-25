import requests
from .utils import BASE_URL


def rerank(
    secret_key,
    query,
    docs,
    num_results=10,
    vec_sample_size=35,
    public_metadata_field="metadata",
    key_field="id",
    plaintext_sample_size=5,
    text_field="text",
    expand=False,
    version="v1",
):
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/rerank"

    payload = {
        "query": query,
        "text_field": text_field,
        "public_metadata_field": public_metadata_field,
        "plaintext_sample_size": plaintext_sample_size,
        "num_results": num_results,
        "vec_sample_size": vec_sample_size,
        "key_field": key_field,
        "docs": docs,
        "expand": expand,
    }

    body = {k: v for k, v in payload.items() if v is not None}

    response = requests.post(url, json=body, headers=headers)
    return response
