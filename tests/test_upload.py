import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestUpload(unittest.TestCase):
    def test_upload_single(self):
        test_str_data = "test"
        test_single_metadata = {"test": "metadata"}

        doc_id = "test_doc_id"

        sub_org_id = "c3f56583-625e-43b3-89aa-970b24232600"
        result = pongo_client.upload(
            # sub_org_id=sub_org_id,
            source_name="test",
            parent_id=doc_id,
            data=test_str_data,
            metadata=test_single_metadata,
        )
        assert result.status_code == 200

    def test_upload_multiple(self):
        test_list_data = ["test", "data"]
        test_list_metadata = {"test2": "metadata2"}

        doc_id = "test_doc_id_lst"

        sub_org_id = "c3f56583-625e-43b3-89aa-970b24232600"
        result = pongo_client.upload(
            # sub_org_id=sub_org_id,
            source_name="test",
            parent_id=doc_id,
            data=test_list_data,
            metadata=test_list_metadata,
        )
        assert result.status_code == 200

    def test_upload_bad_auth(self):
        test_list_data = ["test", "data"]
        test_list_metadata = [{"test1": "metadata1"}, {"test2": "metadata2"}]

        sub_org_id = "c3f56583-625e-43b3-89aa-970b24232600"
        result = pongo_client.upload(
            # sub_org_id=sub_org_id,
            source_name="test",
            data=test_list_data,
            metadata=test_list_metadata,
        )
        assert result.status_code == 404

    def test_upload_bad_org(self):
        test_list_data = ["test", "data"]
        test_list_metadata = [{"test1": "metadata1"}, {"test2": "metadata2"}]

        sub_org_id = "DNE"
        result = pongo_client.upload(
            sub_org_id=sub_org_id,
            source_name="test",
            data=test_list_data,
            metadata=test_list_metadata,
        )
        assert result.status_code == 404


if __name__ == "__main__":
    unittest.main()
