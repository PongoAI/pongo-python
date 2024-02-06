import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestSubOrg(unittest.TestCase):
    def test_get_one(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get_sub_org(
            sub_org_id="4d32dbd3-da6a-451e-8d8c-0dd418b49779",
        )
        assert res.status_code == 200

    def test_get_all(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get_sub_orgs()
        assert res.status_code == 200

    def test_create(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.create_sub_org(
            sub_org_name="test_sub_org 1",
        )
        assert res.status_code == 200

    def test_update(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.update_sub_org(
            sub_org_name="yeehaw boys",
            sub_org_id="4d32dbd3-da6a-451e-8d8c-0dd418b49779",
        )
        assert res.status_code == 200

    def test_delete(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.delete_sub_org(
            sub_org_id="4a2862e0-0260-4474-b534-1ac8f9b1db0a",
        )
        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
