import unittest
import pongo
from dotenv import load_dotenv
import os
import json

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestGet(unittest.TestCase):
    def test_single(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            sub_org_id="351989f7-0e84-4009-8ec4-ead4463e60a8",
            doc_id="bf9b5113-4a26-315e-a7d3-bc5910fb7ef6",
        )

        assert res.status_code == 200

    def test_get_parent(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get(
            sub_org_id="351989f7-0e84-4009-8ec4-ead4463e60a8",
            parent_id="test_lvmh_doc",
        )

        assert len(res.json()) == 173
        assert res.json()[0]["doc_index"] == 0

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
