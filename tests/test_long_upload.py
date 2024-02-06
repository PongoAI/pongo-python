import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestLongUpload(unittest.TestCase):
    def test_upload_long(self):
        test_long_doc = open("./ignore/acquired_transcripts/LVMH.txt", "r").read()
        test_pdf_metadata = {"uploaded_by": "caleb", "parent_id": "test_lvmh_doc", "source": "LVMH Podcast"}
        sub_org_id = "351989f7-0e84-4009-8ec4-ead4463e60a8"
        result = pongo_client.upload(
            sub_org_id=sub_org_id,
            data=test_long_doc,
            metadata=test_pdf_metadata,
        )
        assert result.status_code == 200


if __name__ == "__main__":
    unittest.main()
