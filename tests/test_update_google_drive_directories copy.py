import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")


class TestAuth(unittest.TestCase):
    def test_auth(self):
        pongo_client = pongo.PongoClient(PONGO_SECRET)

        drive_dirs = [
            {
                "id": "1JHzi2q7GvVLVxaqW_xiWjW6rWMzmsdhg",
                "name": "Google Drive Stress Test",
                "enabled": False,
            },
            {
                "id": "1Kcd9m1MUrSQZE2WHeaZxWyyGmyuGFvrI",
                "name": "Testing Private Folder",
                "enabled": False,
            },
            {
                "id": "163iWAeNyMmcLSZHdz4WBL73eKoCVckiS",
                "name": "A 2.06.23 - Intro to Portfolio Services",
                "enabled": False,
            },
            {
                "id": "19paO5RcRv1B0QX3XERy1OBiHNshuJ12w",
                "name": "11.2.22 - Workshop: Cold Outreach Mastery w/ Alex Guest",
                "enabled": False,
            },
            {
                "id": "1qkJak68QsNaGjFw0IEK3Pj4rhe8KLi4K",
                "name": "Pitch Practice Recordings",
                "enabled": False,
            },
            {
                "id": "1VYQDLLdV30tsscVtnAJfCoIy4uIi-4Ah",
                "name": "Article Images",
                "enabled": False,
            },
            {
                "id": "1FK5k7TjejsAOzFHLa-Ulq2TH0eK6S9S6",
                "name": "Pongo",
                "enabled": False,
            },
            {
                "id": "1JUP4061S9GXaiI9xAo9wfntPDpTdElcZ",
                "name": "2022 Seattle T6 Program Resources",
                "enabled": False,
            },
            {
                "id": "1K6H1bxyECZPxCEOn8ZPaTZfw-sfZBlac",
                "name": "landing elements",
                "enabled": False,
            },
            {
                "id": "1vaK333XCZzTL7R3r5sbipXwsrFYDl1-p",
                "name": "design",
                "enabled": False,
            },
            {
                "id": "1FCaxayOwrAibKh_41_P00jmUIqwy7JFQ",
                "name": "Weekly Updates Examples (Full Program)",
                "enabled": False,
            },
            {
                "id": "1dw8F-7JXOQnyWy-H-xlZ3mKXGsWIa_Ku",
                "name": "Guru Logos (SVG, Vector Files)",
                "enabled": False,
            },
        ]

        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.update_drive_directories(
            drive_dirs, "c6d6f914-a08d-4529-9602-e80bd418885c"
        )

        assert res.status_code == 200
        body = res.json()
        assert "error" not in body


if __name__ == "__main__":
    unittest.main()
