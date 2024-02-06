import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestAuth(unittest.TestCase):
    def test_auth(self):
        # Ensure that the client is initialized properly and connected to server
        heartbeat = pongo_client.heartbeat()
        assert heartbeat.status_code == 200


if __name__ == "__main__":
    unittest.main()
