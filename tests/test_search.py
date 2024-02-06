import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestSearch(unittest.TestCase):
    def test_search(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.search(
            sub_org_id="351989f7-0e84-4009-8ec4-ead4463e60a8",
            query="When did LVMH start YSL?",
            num_results=5,
            sample_size=5,
        )

        assert len(res.json()) == 5

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
