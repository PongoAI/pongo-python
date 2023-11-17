import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()

PONGO_PUBLIC = os.getenv("PONGO_PUBLIC")
PONGO_SECRET = os.getenv("PONGO_SECRET")
pongo_client = pongo.PongoClient(PONGO_PUBLIC, PONGO_SECRET)
class TestUpload(unittest.TestCase):
    def test_upload_single(self):

        test_str_data = "test"
        test_single_metadata = {"test": "metadata"}

        doc_id = "test_doc_id"

        sub_org_id = "9ce132df-4360-4c38-8a36-016cd66c678d"
        result = pongo_client.upload(sub_org=sub_org_id, source_name="test", parent_id=doc_id, data=test_str_data, metadata=test_single_metadata)
        assert result.status_code == 200
    
    def test_upload_multiple(self):
        test_list_data = ["test", "data"]
        test_list_metadata = {"test2": "metadata2"}

        doc_id = "test_doc_id_lst"

        sub_org_id = "db819b57-1350-4110-9d7c-063c3d49b96e"
        result = pongo_client.upload(sub_org=sub_org_id, source_name="test", parent_id=doc_id ,data=test_list_data, metadata=test_list_metadata)
        assert result.status_code == 200
    
    def test_upload_bad_auth(self):
        test_list_data = ["test", "data"]
        test_list_metadata = [{"test1": "metadata1"}, {"test2": "metadata2"}]

        sub_org_id = "b597bc44-d573-4b4b-83d8-6c1ec8660f3f"
        result = pongo_client.upload(sub_org=sub_org_id, source_name="test", data=test_list_data, metadata=test_list_metadata)
        assert result.status_code == 401
    
    def test_upload_bad_org(self):
        test_list_data = ["test", "data"]
        test_list_metadata = [{"test1": "metadata1"}, {"test2": "metadata2"}]

        sub_org_id = "DNE"
        result = pongo_client.upload(sub_org=sub_org_id, source_name="test", data=test_list_data, metadata=test_list_metadata)
        assert result.status_code == 404
        

if __name__ == '__main__':
    unittest.main()
