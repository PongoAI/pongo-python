import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")

class TestUpload(unittest.TestCase):
    def test_upload_single(self):
        pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)
        test_str_data = "test"
        test_single_metadata = {"test": "metadata"}
        result = pongo_client.upload(sub_org="test", source_name="test", data=test_str_data, metadata=test_single_metadata)
        assert result.status_code == 200
    
    def test_upload_multiple(self):
        pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)
        test_list_data = ["test", "data"]
        test_list_metadata = [{"test1": "metadata1"}, {"test2": "metadata2"}]

        result = pongo_client.upload(sub_org="test", source_name="test", data=test_list_data, metadata=test_list_metadata)
        assert result.status_code == 200
        

if __name__ == '__main__':
    unittest.main()
