import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET =  '7309ef003c354494b6f3f8b6951b857f'

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestSearch(unittest.TestCase):
    def test_search(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.rerank(
            docs=[
                {"ig": 1, "text": "Roses are red", "betadata": {}},
                {"ig": 2, "text": "Violets are blue", "betadata": {}},
                {"ig": 3, "text": "Roses are red2", "betadata": {}},
                {"ig": 4, "text": "Roses are red3", "betadata": {}},
            ],
            num_results=3,
            query="what color are roses?",
            public_metadata_field="betadata",
            key_field="ig",
        )

        print(res.json())

        assert len(res.json()) == 3

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
