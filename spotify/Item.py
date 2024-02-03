import json
from .Requests import Requests

class Item:
    def __init__(self, endpoint, response, requests):
        self.requests = requests
        #self.endpoints = requests.endpoints
        self.response = response
        self.url = self.response["external_urls"]["spotify"]
        self.id = self.response["id"]
        self.name = self.response["name"]
        self.endpoint = endpoint
        #self.access_token = requests.access_token

    def get(self, item_id, endpoint=None):
        if not endpoint:
            endpoint = self.endpoint
        return self.requests.get(endpoint, item_id)


