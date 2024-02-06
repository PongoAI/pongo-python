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
        res = pongo_client.get_auth_link("123", "GitHub", "google.com")

        assert res.status_code == 200
        body = res.json()
        assert "error" not in body
        assert "auth_link" in body


if __name__ == "__main__":
    unittest.main()
