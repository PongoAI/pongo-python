import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")


class TestAuth(unittest.TestCase):
    def test_auth(self):
        pongo_client = pongo.PongoClient(PONGO_SECRET)

        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.disconnect_integration(
            "395d0830-980b-41e9-88dd-06e3ec4642ff", "Google Drive"
        )
        body = res.json()
        assert res.status_code == 200
        assert "error" not in body


if __name__ == "__main__":
    unittest.main()
