import json
from typing import Any, Dict, List
import requests
from .utils import BASE_URL
import gzip


def observe(
    secret_key: str,
    query: str,
    docs: List[str],
    log_metadata: Dict[str, Any] = None,
    version: str = "v1",
):
    headers = {
        "secret": secret_key,
        "Content-Encoding": "gzip",
        "Content-Type": "application/json",
    }
    url = f"{BASE_URL}/api/{version}/observe"

    payload = {
        "query": query,
        "docs": docs,
        "log_metadata": log_metadata,
    }

    body = {k: v for k, v in payload.items() if v is not None}

    # Serialize the data to JSON format
    json_data = json.dumps(body).encode("utf-8")

    # Compress the JSON data using gzip
    compressed_data = gzip.compress(json_data)

    response = requests.post(url, data=compressed_data, headers=headers)
    return response
