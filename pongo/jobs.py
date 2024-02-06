import requests
from .utils import BASE_URL


def get_job(
    secret_key,
    sub_org_id=None,
    job_id=None,
    version="v1",
):
    """
    Retrieves a single job from the Pongo API.
    :param job_id: ID of the job to be retrieved.
    :param sub_org_id: Optional- ID of the organization to pull the job from.  If no id is provided, the main organization's ID will be used.
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/job"

    if not job_id:
        raise Exception("Must provide job_id")

    payload = {
        "sub_org_id": sub_org_id,
        "job_id": job_id,
    }

    params = {key: value if not isinstance(value, list) else ','.join(value) for key, value in payload.items() if value is not None}
    response = requests.get(url, headers=headers, params=params)
    return response

def get_jobs(
    secret_key,
    job_status,
    sub_org_id=None,
    page=0,
    version="v1",
):
    """
    Retrieves a list of jobs from the Pongo in paginated format.
    :param job_status: Status of jobs to retreive.  Options are "*", "queued", "processing", and "processed".
    :param sub_org_id: Optional- ID of the organization to pull the job from.  If no id is provided, the main organization's ID will be used.
    """
    headers = {
        "secret": secret_key,
    }
    url = f"{BASE_URL}/api/{version}/jobs"

    if not job_status:
        raise Exception("Must provide job_status")

    payload = {
        "sub_org_id": sub_org_id,
        "job_status": job_status,
        "page": page
    }

    params = {key: value if not isinstance(value, list) else ','.join(value) for key, value in payload.items() if value is not None}
    response = requests.get(url, headers=headers, params=params)
    return response