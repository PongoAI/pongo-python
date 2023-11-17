import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")
pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)
class TestSubOrg(unittest.TestCase):
    def test_get_one(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get_sub_orgs(
            sub_org="db819b57-1350-4110-9d7c-063c3d49b96e",
        )
        assert res.status_code == 200
    
    def test_get_all(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.get_sub_orgs()
        assert res.status_code == 200
    
    def test_create(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.create_sub_org(
            sub_org_name="test_sub_org",
        )
        assert res.status_code == 200
    
    def test_delete(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.delete_sub_org(
            sub_org="e6a64705-4da9-4429-b75c-553faa987e2b",
        )
        assert res.status_code == 200

if __name__ == '__main__':
    unittest.main()
