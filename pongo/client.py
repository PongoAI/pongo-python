from .upload import upload, upload_pdf
from .scrape import scrape_website
from .integrations.get_auth_link import get_auth_link
from .integrations.update_drive_directories import update_drive_directories
from .integrations.disconnect_integration import disconnect_integration
from .search import search
from .get import get
from .delete import delete
from .org_management import create_sub_org, get_sub_orgs, delete_sub_org, update_sub_org
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

    def search(
        self,
        sub_org_id,
        query,
        start_time=None,
        end_time=None,
        sources=[],
        num_results=15,
        max_reranker_results=5,
    ):
        """
        Searches for data in the Pongo API.
        OPTIONAL: start_time, end_time, sources
        """
        return search(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            query=query,
            sources=sources,
            start_time=start_time,
            end_time=end_time,
            num_results=num_results,
            max_reranker_results=max_reranker_results,
            version=self.version,
        )

    def get(self, sub_org_id, doc_id=None, parent_id=None):
        """
        Retrieves a single document chunk or a list of document chunks from the Pongo API.
        :param doc_id: ID of the document to be retrieved.
        :param parent_id: ID of the parent document to be retrieved. Will return all chunks of the parent document.
        """
        return get(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            doc_id=doc_id,
            parent_id=parent_id,
            version=self.version,
        )

    def upload(
        self, sub_org_id, source_name, data, parent_id=None, metadata={}, timestamp=None
    ):
        """
        Uploads a data to pongo for semantic search.
        :param sub_org_id: Sub organization of the data.
        :param source_name: Name of the source of the data.
        :param data: Data to be uploaded. Can be a single string or a list of strings.
        :param metadata: Metadata for the data. Can be a single dictionary or a list of dictionaries.
        :param timestamp: Timestamp for the data. Defaults to the current time.
        :return: Response from the server.
        """

        return upload(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            source_name=source_name,
            data=data,
            metadata=metadata,
            timestamp=timestamp,
            parent_id=parent_id,
            version=self.version,
        )
    
    def upload_pdf(
        self, sub_org_id, source_name, file_path, parent_id=None, metadata={}, timestamp=None
    ):
        """
        Uploads a pdf to pongo for semantic search.
        :param sub_org_id: Sub organization of the data.
        :param source_name: Name of the source of the data.
        :param data: Data to be uploaded. Can be a single string or a list of strings.
        :param metadata: Metadata for the data. Can be a single dictionary or a list of dictionaries.
        :param timestamp: Timestamp for the data. Defaults to the current time.
        :return: Response from the server.
        """

        return upload_pdf(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            source_name=source_name,
            file_path=file_path,
            metadata=metadata,
            timestamp=timestamp,
            parent_id=parent_id,
            version=self.version,
        )

    def delete(self, sub_org_id, doc_id=None, parent_id=None):
        """
        Deletes a single document chunk or a list of document chunks from the Pongo API.
        :param doc_id: ID of the document to be deleted.
        :param parent_id: ID of the parent document to be deleted. Will delete all chunks of the parent document.
        """
        return delete(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            doc_id=doc_id,
            parent_id=parent_id,
            version=self.version,
        )

    def scrape_website(self, sub_org_id, site_name, site_url):
        """
        Uploads a data to pongo for semantic search.
        :param sub_org_id: Sub organization of the data.
        :param source_name: Name of the source of the data.
        :param data: Data to be uploaded. Can be a single string or a list of strings.
        :param metadata: Metadata for the data. Can be a single dictionary or a list of dictionaries.
        :param timestamp: Timestamp for the data. Defaults to the current time.
        :return: Response from the server.
        """

        return scrape_website(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            site_name=site_name,
            site_url=site_url,
            version=self.version,
        )

    def get_auth_link(self, sub_org_id, integration_name, redirect_uri):
        """
        Generates a link that sub-organizations can use to authenticate with other platforms and have their data ingested by Pongo.

        :param sub_org_id: ID of the sub-organization to generate a link for
        :param integration_name: Name of the integration to authenticate with
        :param redirect_uri: The address users will be sent to after completing the authentication process- wether successful or unsuccessful.
        :return: Response from the server containing the authentication link or error message.
        """
        return get_auth_link(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            integration_name=integration_name,
            redirect_uri=redirect_uri,
            version=self.version,
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
            secret_key=self._secret_key,
            new_dirs=new_dirs,
            integration_id=integration_id,
            version=self.version,
        )

    def disconnect_integration(
        self,
        integration_id,
        integration_name,
    ):
        """
        Disconnect an integration and delete all of its data

        :param integration_id: ID of the integration to delete
        :param name: Name of the integration to delete
        :return: Response from the server which may contain a disconnect link for the end user, depending on the integration.
        """
        return disconnect_integration(
            public_key=self.user_id,
            secret_key=self._secret_key,
            integration_id=integration_id,
            integration_name=integration_name,
            version=self.version,
        )


    def create_sub_org(self, sub_org_name):
        """
        Creates a sub org, with a given name, returns the sub org id and metadata.
        """
        return create_sub_org(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_name=sub_org_name,
            version=self.version,
        )
    def update_sub_org(self, sub_org_id, sub_org_name):
        """
        Update a sub org's name
        """
        return update_sub_org(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_name=sub_org_name,
            sub_org_id=sub_org_id,
            version=self.version,
        )
    
    def get_sub_orgs(self):
        """
        Returns list of all sub orgs.
        """
        return get_sub_orgs(
            public_key=self.user_id,
            secret_key=self._secret_key,
            version=self.version,
        )

    def get_sub_org(self, sub_org_id):
        """
        Retrieves a sub org by ID
        """
        return get_sub_orgs(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            version=self.version,
        )
    

    def delete_sub_org(self, sub_org_id):
        """
        Delete a sub org by ID.
        Will also delete all data associated with the sub org.
        """
        return delete_sub_org(
            public_key=self.user_id,
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            version=self.version,
        )
