from .upload import upload
from .scrape import scrape_website
from .utils import BASE_URL
import requests


class PongoClient:
    def __init__(self, user_id, secret_key, version="v1"):
        """
        Initializes a PongoClient object.
        :param user_id: User ID. This looks like pongo_public_....
        :param secret_key: Secret key. This looks like pongo_secret_*****
        """
        self.user_id = user_id
        self._secret_key = secret_key
        self.version = version

        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self._secret_key, "id": self.user_id}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")

    def heartbeat(self):
        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self._secret_key, "id": self.user_id}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")
        else:
            return response

    def upload(self, sub_org, source_name, data, parent_id=None, metadata={}, timestamp=None):
        """
        Uploads a data to pongo for semantic search.
        :param sub_org: Sub organization of the data.
        :param source_name: Name of the source of the data.
        :param data: Data to be uploaded. Can be a single string or a list of strings.
        :param metadata: Metadata for the data. Can be a single dictionary or a list of dictionaries.
        :param timestamp: Timestamp for the data. Defaults to the current time.
        :return: Response from the server.
        """

        return upload(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org=sub_org,
            source_name=source_name,
            data=data,
            metadata=metadata,
            timestamp=timestamp,
            parent_id=parent_id,
            version=self.version,
        )


    def scrape_website(self, sub_org, site_name, site_url):
        """
        Uploads a data to pongo for semantic search.
        :param sub_org: Sub organization of the data.
        :param source_name: Name of the source of the data.
        :param data: Data to be uploaded. Can be a single string or a list of strings.
        :param metadata: Metadata for the data. Can be a single dictionary or a list of dictionaries.
        :param timestamp: Timestamp for the data. Defaults to the current time.
        :return: Response from the server.
        """

        return scrape_website(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org=sub_org,
            site_name=site_name,
            site_url=site_url,
            version=self.version,
        )
