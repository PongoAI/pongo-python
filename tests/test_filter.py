import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")
pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestFilter(unittest.TestCase):
    def test_filter(self):
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.filter(
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

    def test_filter_with_observe_dict(self):
        res = pongo_client.filter(
            docs=[
                {"id": "a", "text": "The sky is gray"},
                {"id": "b", "text": "I am an orangutan"},
                {"id": "c", "text": "Roses are red"},
                {"id": "d", "text": "Roses are native to Asia"},
                {"id": "e", "text": "Violets are blue"},
            ],
            query="what color are roses?",
            observe=True,
        )

        print(res.json())

        assert res.status_code == 200

    def test_filter_with_observe_list(self):
        res = pongo_client.filter(
            docs=[
                "The sky is gray",
                "I am an orangutan",
                "Roses are red",
                "Roses are native to Asia",
                "Violets are blue",
            ],
            query="what color are roses?",
            observe=True,
        )

        print(res.json())

        assert res.status_code == 200

    def test_filter_with_observe_log_metadata(self):
        res = pongo_client.filter(
            docs=[
                "The sky is gray",
                "I am an orangutan",
                "This has log metadata",
                "Pandas eat bamboo" "Orangutans are from Borneo",
                "There are no roses in Australia",
            ],
            query="what color are roses?",
            log_metadata={
                "user_id": "1",
                "session_id": "4",
            },
            observe=True,
        )

        print(res.json())

        assert res.status_code == 200


if __name__ == "__main__":
    unittest.main()
