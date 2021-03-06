# coding=utf-8
"""Implementation of GeoNode Maps API endpoint.
"""
from geonode_api.api_client import ApiClient

class MapAPI(ApiClient):
    """
     Managing GeoNode Maps API endpoints

    """

    def __init__(self, endpoint_url ):
        """Implementation of GeoNode maps API client.

        API base url.
        :type endpoint_url: str
        """
        super(LayerAPI, self).__init__( endpoint_url)

    @property
    def base_url(self):
        """Base url of the API.

        :return: API url.
        :rtype: str
        """
        return '%s/layers/v2' % (self.endpoint_url)

    def get_maps(self, endpoint):
        """Abstract.
        """

        response = self.get(endpoint)
        return response.json()

