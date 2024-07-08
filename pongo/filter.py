import json
import requests
from .utils import BASE_URL
import gzip


def filter(
    secret_key,
    query,
    docs,
    num_results=10,
    vec_sample_size=35,
    public_metadata_field="metadata",
    key_field="id",
    plaintext_sample_size=5,
    text_field="text",
    log_metadata=None,
    observe=False,
    version="v1",
):
    headers = {
        "secret": secret_key,
        "Content-Encoding": "gzip",
        "Content-Type": "application/json",
    }
    url = f"{BASE_URL}/api/{version}/filter"

    payload = {
        "query": query,
        "text_field": text_field,
        "public_metadata_field": public_metadata_field,
        "plaintext_sample_size": plaintext_sample_size,
        "num_results": num_results,
        "vec_sample_size": vec_sample_size,
        "key_field": key_field,
        "docs": docs,
        "log_metadata": log_metadata,
        "observe": observe,
    }

    body = {k: v for k, v in payload.items() if v is not None}

    # Serialize the data to JSON format
    json_data = json.dumps(body).encode("utf-8")

    # Compress the JSON data using gzip
    compressed_data = gzip.compress(json_data)

    response = requests.post(url, data=compressed_data, headers=headers)
    return response
