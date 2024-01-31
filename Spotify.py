from Auth import Auth
from Search import Search
from Get import Get
import os

class Spotify:
    def __init__(self, client_id, client_secret):
        self.endpoints = self.loadEndpoints()
        self.auth = Auth(client_id, client_secret, self.endpoints)
        self.access_token = self.auth.getAccessToken()
        self.search = Search(self.access_token, self)
        self.get = Get(self.access_token, self.endpoints)

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