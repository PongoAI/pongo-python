import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")
pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)


class TestDelete(unittest.TestCase):
    def test_single(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.delete(
            sub_org="9ce132df-4360-4c38-8a36-016cd66c678d",
            doc_id="06e1b73b-6953-33a4-bdd0-7e2854b94c0f",
        )

        print(res.json())
        assert res.status_code == 200
    
    def test_get_parent(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.delete(
            sub_org="9ce132df-4360-4c38-8a36-016cd66c678d",
            parent_id="b11f2e55-0ad7-428b-9813-2d78e9e3009d",
        )

        print(res.json())
        assert res.status_code == 200






if __name__ == "__main__":
    unittest.main()
