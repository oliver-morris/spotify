from spotify.Auth import Auth
from spotify.Search import Search
from spotify.Get import Get
import os
from spotify.Requests import Requests
from spotify.ItemList import ItemList

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