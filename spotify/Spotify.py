from .Auth import Auth
from .Search import Search
from .Get import Get
import os
from .Requests import Requests
from .ItemList import ItemList

class Spotify:
    def __init__(self, client_id, client_secret):
        endpoints = self.loadEndpoints()
        auth = Auth(client_id, client_secret, endpoints)
        access_token = auth.getAccessToken()
        self.requests = Requests(endpoints, access_token)
        self.search = Search(self.requests)
        self.get = Get(self.requests)

    def loadEndpoints(self):
        try:
            import tomllib as toml
        except ModuleNotFoundError:
            import tomli as toml

        config_file = os.path.abspath(os.path.dirname(__file__)) + "\\endpoints.toml"
        with open(config_file, "rb") as config_file:
          config = toml.load(config_file)
          config_file.close()

        return config