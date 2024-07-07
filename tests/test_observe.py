import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_SECRET = os.getenv("PONGO_KEY")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestObserve(unittest.TestCase):
    def test_observe(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.observe(
            query="what color are roses?",
            docs=[
                "The sky is gray",
                "Roses are red",
                "This has log metadata",
                "Roses are native to Asia",
                "Violets are blue",
            ],
            log_metadata={"user_source": "web"},
        )
        print(res.json())

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
