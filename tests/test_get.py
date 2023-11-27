import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")
pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)


class TestGet(unittest.TestCase):
    def test_single(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            doc_id="8b8a322c-31e2-3283-9838-a3dc1fe4de85",
        )

        assert res.status_code == 200
    
    def test_get_parent(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            parent_id="64d83ed3-c875-4677-b95b-a8c7bf716882",
        )

        assert res.status_code == 200






if __name__ == "__main__":
    unittest.main()
