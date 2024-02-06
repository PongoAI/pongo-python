import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestWebScrape(unittest.TestCase):
    def test_scrape(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.scrape_website(
            "9ce132df-4360-4c38-8a36-016cd66c678d",
            "test_site",
            "https://www.marchex.com/",
        )

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
