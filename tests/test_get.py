import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_SECRET")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestGet(unittest.TestCase):
    def test_single(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            # sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            doc_id="be738d73-3326-35bb-825c-9b59a489bace",
        )

        assert res.status_code == 200

    def test_get_parent(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            # sub_org_id="9ce132df-4360-4c38-8a36-016cd66c678d",
            parent_id="0107f9fc-5a15-4e41-a61e-8ecd41902cf6",
        )

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
