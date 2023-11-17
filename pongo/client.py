from .upload import upload
from .integrations.get_auth_link import get_auth_link
from .integrations.update_drive_directories import update_drive_directories
from .integrations.disconnect_integration import disconnect_integration
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
        self.secret_key = secret_key
        self.version = version

        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self.secret_key, "id": self.user_id}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")

    def heartbeat(self):
        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self.secret_key, "id": self.user_id}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")
        else:
            return response

    def upload(self, sub_org, source_name, data, metadata={}, timestamp=None):
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
            secret_key=self.secret_key,
            sub_org=sub_org,
            source_name=source_name,
            data=data,
            metadata=metadata,
            timestamp=timestamp,
            version=self.version,
        )

    def get_auth_link(self, id,integration_name,redirect_uri):
        """
        Generates a link that sub-organizations can use to authenticate with other platforms and have their data ingested by Pongo.

        :param id: ID of the sub-organization to generate a link for
        :param integration_name: Name of the integration to authenticate with
        :param redirect_uri: The address users will be sent to after completing the authentication process- wether successful or unsuccessful.
        :return: Response from the server containing the authentication link or error message.
        """
        return get_auth_link(
        public_key=self.user_id,
        secret_key=self.secret_key,
        id=id,
        integration_name=integration_name,
        redirect_uri=redirect_uri,
        version=self.version
        )

    def update_drive_directories(self, new_dirs, integration_id):
        """
        Generates a link that sub-organizations can use to authenticate with other platforms and have their data ingested by Pongo.

        :param integration_id: ID of the google drive integration to update
        :param new_dirs: Array containing the new "enabled" states of google drive directories, id's and length must be the same
        :param redirect_uri: The address users will be sent to after completing the authentication process- wether successful or unsuccessful.
        :return: Response from the server containing the authentication link or error message.
        """
        return update_drive_directories(
        public_key=self.user_id,
        secret_key=self.secret_key,
        new_dirs=new_dirs,
        integration_id=integration_id,
        version=self.version
        )
    def disconnect_integration(self, id, name,):
        """
        Disconnect an integration and delete all of its data

        :param id: ID of the integration to delete
        :param name: Name of the integration to delete
        :return: Response from the server which may contain a disconnect link for the end user, depending on the integration.
        """
        return disconnect_integration(
        public_key=self.user_id,
        secret_key=self.secret_key,
        id=id,
        name=name,
        version=self.version)
