from .upload import upload, upload_pdf
from .scrape import scrape_website
from .integrations.get_auth_link import get_auth_link
from .integrations.update_drive_directories import update_drive_directories
from .integrations.disconnect_integration import disconnect_integration
from .search import search
from .get import get
from .delete import delete
from .org_management import create_sub_org, get_sub_orgs, delete_sub_org, update_sub_org
from .jobs import get_job, get_jobs
from .utils import BASE_URL
import requests


class PongoClient:
    def __init__(self, secret_key, version="v1"):
        """
        Initializes a PongoClient object.
        :param secret_key: Secret API key.
        """
        self._secret_key = secret_key
        self.version = version

        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self._secret_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")

    def heartbeat(self):
        url = f"{BASE_URL}/api/{self.version}/authorize_user"
        headers = {"secret": self._secret_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            raise Exception("Invalid credentials")
        elif response.status_code == 500:
            raise Exception("Server error")
        else:
            return response

    def search(
        self,
        query,
        sub_org_id=None,
        start_time=None,
        end_time=None,
        sources=[],
        num_results=10,
        sample_size=15,
    ):
        """
        Searches for data in the Pongo API.
        OPTIONAL: start_time, end_time, sources
        """
        return search(
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            query=query,
            sources=sources,
            start_time=start_time,
            end_time=end_time,
            num_results=num_results,
            sample_size=sample_size,
            version=self.version,
        )

    def get(self, sub_org_id=None, doc_id=None, parent_id=None):
        """
        Retrieves a single document chunk or a list of document chunks from the Pongo API.
        :param doc_id: ID of the document to be retrieved.
        :param parent_id: ID of the parent document to be retrieved. Will return all chunks of the parent document.
        """
        return get(
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            doc_id=doc_id,
            parent_id=parent_id,
            version=self.version,
        )

    def upload(self, data, sub_org_id=None, metadata={}, timestamp=None):
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
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            data=data,
            metadata=metadata,
            timestamp=timestamp,
            version=self.version,
        )

    def upload_pdf(
        self,
        source_name,
        file_path,
        sub_org_id=None,
        parent_id=None,
        metadata={},
        timestamp=None,
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
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            source_name=source_name,
            file_path=file_path,
            metadata=metadata,
            timestamp=timestamp,
            parent_id=parent_id,
            version=self.version,
        )

    def delete(self, sub_org_id=None, doc_id=None, parent_id=None):
        """
        Deletes a single document chunk or a list of document chunks from the Pongo API.
        :param doc_id: ID of the document to be deleted.
        :param parent_id: ID of the parent document to be deleted. Will delete all chunks of the parent document.
        """
        return delete(
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            doc_id=doc_id,
            parent_id=parent_id,
            version=self.version,
        )

    def scrape_website(self, site_name, site_url, sub_org_id=None):
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
            secret_key=self._secret_key,
            sub_org_name=sub_org_name,
            version=self.version,
        )

    def update_sub_org(self, sub_org_id, sub_org_name):
        """
        Update a sub org's name
        """
        return update_sub_org(
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
            secret_key=self._secret_key,
            version=self.version,
        )

    def get_sub_org(self, sub_org_id):
        """
        Retrieves a sub org by ID
        """
        return get_sub_orgs(
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
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            version=self.version,
        )
    def get_jobs(self, job_status, sub_org_id=None, page=0):
        """
        Retrieves a list of jobs from the Pongo in paginated format.
        :param job_status: Status of jobs to retreive.  Options are "*", "queued", "processing", and "processed".
        :param sub_org_id: Optional- ID of the organization to pull the job from.  If no id is provided, the main organization's ID will be used.
        """
        return get_jobs(
            secret_key=self._secret_key,
            job_status=job_status,
            sub_org_id=sub_org_id,
            page=page,
            version=self.version,
        )

    def get_job(self, job_id, sub_org_id=None):
        """
        Retrieves a single job from the Pongo API.
        :param job_id: ID of the job to be retrieved.
        :param sub_org_id: Optional- ID of the organization to pull the job from.  If no id is provided, the main organization's ID will be used.
        """
        return get_job(
            secret_key=self._secret_key,
            sub_org_id=sub_org_id,
            job_id=job_id,
            version=self.version,
        )
