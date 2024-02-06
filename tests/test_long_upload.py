import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_SECRET")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestLongUpload(unittest.TestCase):
    def test_upload_long(self):
        test_long_doc = open("./ignore/acquired_transcripts/LVMH.txt", "r").read()
        test_pdf_metadata = {"uploaded_by": "caleb"}
        doc_id = "test_lvmh_doc"
        sub_org_id = "db819b57-1350-4110-9d7c-063c3d49b96e"
        result = pongo_client.upload(
            sub_org_id=sub_org_id,
            source_name="LVMH pod",
            parent_id=doc_id,
            data=test_long_doc,
            metadata=test_pdf_metadata,
        )
        assert result.status_code == 200


if __name__ == "__main__":
    unittest.main()
