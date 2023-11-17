import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")
class TestAuth(unittest.TestCase):
    def test_auth(self):
        pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)

        
        # Ensure that the client is initialized properly and connected to server
        res = pongo_client.disconnect_integration('c6d6f914-a08d-4529-9602-e80bd418885c', 'Google Drive') 
        body = res.json()
        assert res.status_code == 200
        assert 'error' not in body

if __name__ == '__main__':
    unittest.main()
