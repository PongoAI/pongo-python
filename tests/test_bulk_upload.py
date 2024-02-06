import unittest
import pongo
from dotenv import load_dotenv
import os

load_dotenv()


PONGO_SECRET = os.getenv("PONGO_KEY")

pongo_client = pongo.PongoClient(PONGO_SECRET)


class TestLongUpload(unittest.TestCase):
    def test_upload_long(self):
        filenames = [
            "./ignore/acquired_transcripts/Airbnb.txt",
            "./ignore/acquired_transcripts/Android.txt",
            "./ignore/acquired_transcripts/Costco.txt",
        ]
        data = []
        metadata = []
        for filename in filenames:
            test_long_doc = open(filename, "r").read()
            parent_id = filename.split("/")[-1].split(".")[0].lower()
            source = filename.split("/")[-1].split(".")[0]
            test_pdf_metadata = {"uploaded_by": "caleb", "parent_id": parent_id, "source": f"{source} Podcast"}
            sub_org_id = "351989f7-0e84-4009-8ec4-ead4463e60a8"
            data.append(test_long_doc)
            metadata.append(test_pdf_metadata)

        result = pongo_client.upload(
            sub_org_id=sub_org_id,
            data=data,
            metadata=metadata,
        )
        print(result.json())
        assert result.status_code == 200


if __name__ == "__main__":
    unittest.main()
