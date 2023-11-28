import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")

pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)


class TestSearch(unittest.TestCase):
    def test_search(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.search(
            sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            query="How can marchex help automotive dealerships?",
        )

        assert res.status_code == 200
    
    
    def test_search_time_range(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.search(
            sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            query="How can marchex help automotive dealerships?",
            start_time=1600223000,
            end_time=1701223034,
        )   


        assert res.status_code == 200
    
    def test_search_source_list(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.search(
            sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            query="How can marchex help automotive dealerships?",
            sources=["test_site"],
        )

        assert res.status_code == 200




if __name__ == "__main__":
    unittest.main()
