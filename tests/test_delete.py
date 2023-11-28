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
            sub_org_id="c3f56583-625e-43b3-89aa-970b24232600",
            doc_id="1499d8a0-8840-3626-8ca0-394113eff353",
        )

        print(res.json())
        assert res.status_code == 200
    
    def test_delete_parent(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.delete(
            sub_org_id="c3f56583-625e-43b3-89aa-970b24232600",
            parent_id="test_doc_id_lst",
        )

        print(res.json())
        assert res.status_code == 200






if __name__ == "__main__":
    unittest.main()
