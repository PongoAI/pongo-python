import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_SECRET = os.getenv("PONGO_SECRET")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestJobs(unittest.TestCase):
    def test_get_all(self):
        result = pongo_client.get_jobs(
            job_status='*',
        )
        assert result.status_code == 200
    def test_get_processing(self):
        result = pongo_client.get_jobs(
            job_status='processing',
        )
        assert result.status_code == 200
    def test_get_processed(self):
        result = pongo_client.get_jobs(
            job_status='processed',
        )
        assert result.status_code == 200
    def test_get_queued(self):
        result = pongo_client.get_jobs(
            job_status='queued',
        )
        assert result.status_code == 200
    def test_get_page_2(self):
        sub_org_id='9ce132df-4360-4c38-8a36-016cd66c678d'
        result = pongo_client.get_jobs(
            sub_org_id=sub_org_id,
            job_status='*',
        )
        assert result.status_code == 200

    def test_get_specific(self):
        sub_org_id='9ce132df-4360-4c38-8a36-016cd66c678d'
        result = pongo_client.get_job(
            sub_org_id=sub_org_id,
            job_id='job_4b5dcb92-3748-4042-8e5d-5881de463ea4'
        )
        assert result.status_code == 200

    

if __name__ == "__main__":
    unittest.main()
