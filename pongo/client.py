from .utils import BASE_URL
from .rerank import rerank
from .filter import filter
from .observe import observe
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
        url = f"{BASE_URL}/api/{self.version}/"
        response = requests.get(url)
        if response.status_code == 500:
            raise Exception("Server error")
        else:
            return response

    def rerank(
        self,
        query,
        docs,
        num_results=10,
        vec_sample_size=25,
        public_metadata_field="metadata",
        key_field="id",
        plaintext_sample_size=5,
        text_field="text",
        version="v1",
    ):
        """
        ALIAS to filter api
        Reranks the documents provided, reccomended to pass 50-100 results
        :param query - Query used to get the initial results
        :param numResults (optional) - Total number of results to return at the end of the operation
        :param vecSampleSize (optional) - Number of vector results to pass into the reranker at the end of Pongo's workflow
        :param plaintextSampleSize (optional) - Number of plain text results to pass into the reranker at the end of Pongo's workflow
        :param publicMetadataField (optional) - Name of the key in each docs object that contains metadata information to be included in pongo's reranking- defaults to "metadata"
        :param keyField (optional) - Name of the key in each docs object to be used as their id, defaults to "id"
        :param textField (optional) - Name of the key in each docs object to do the reranking on, defaults to "text"
        """
        return rerank(
            secret_key=self._secret_key,
            query=query,
            docs=docs,
            num_results=num_results,
            vec_sample_size=vec_sample_size,
            public_metadata_field=public_metadata_field,
            key_field=key_field,
            plaintext_sample_size=plaintext_sample_size,
            text_field=text_field,
            version=version,
        )

    def filter(
        self,
        query,
        docs,
        num_results=10,
        vec_sample_size=25,
        public_metadata_field="metadata",
        key_field="id",
        plaintext_sample_size=5,
        text_field="text",
        log_metadata=None,
        observe=False,
        version="v1",
    ):
        """
        Semantic filter over the documents provided, recommended to pass 75-150 results
        :param query - Query used to get the initial results
        :param numResults (optional) - Total number of results to return at the end of the operation
        :param vecSampleSize (optional) - Number of vector results to pass into the filter at the end of Pongo's workflow
        :param plaintextSampleSize (optional) - Number of plain text results to pass into the filter at the end of Pongo's workflow
        :param publicMetadataField (optional) - Name of the key in each docs object that contains metadata information to be included in pongo's filtering- defaults to "metadata"
        :param keyField (optional) - Name of the key in each docs object to be used as their id, defaults to "id"
        :param textField (optional) - Name of the key in each docs object to do the filtering on, defaults to "text"
        """
        return filter(
            secret_key=self._secret_key,
            query=query,
            docs=docs,
            num_results=num_results,
            vec_sample_size=vec_sample_size,
            public_metadata_field=public_metadata_field,
            key_field=key_field,
            plaintext_sample_size=plaintext_sample_size,
            text_field=text_field,
            log_metadata=log_metadata,
            observe=observe,
            version=version,
        )

    def observe(
        self,
        query,
        docs,
        log_metadata=None,
        version="v1",
    ):
        return observe(
            secret_key=self._secret_key,
            query=query,
            docs=docs,
            log_metadata=log_metadata,
            version=version,
        )
