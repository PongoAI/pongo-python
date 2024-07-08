import json
from typing import Any, Dict, List, Union
import requests
from .utils import BASE_URL
import gzip


def rerank(
    secret_key: str,
    query: str,
    docs: Union[List[str], List[Dict[str, Any]]],
    num_results: int = 10,
    vec_sample_size: int = 25,
    public_metadata_field: str = "metadata",
    key_field: str = "id",
    plaintext_sample_size: int = 5,
    text_field: str = "text",
    expand: bool = False,
    version: str = "v1",
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
        "expand": expand,
    }

    body = {k: v for k, v in payload.items() if v is not None}

    # Serialize the data to JSON format
    json_data = json.dumps(body).encode("utf-8")

    # Compress the JSON data using gzip
    compressed_data = gzip.compress(json_data)

    response = requests.post(url, data=compressed_data, headers=headers)
    return response
