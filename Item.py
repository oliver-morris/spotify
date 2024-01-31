import requests
import json

class Item:
    def __init__(self, access_token, endpoint, response):
        self.response = response
        self.url = self.response["external_urls"]["spotify"]
        self.id = self.response["id"]
        self.name = self.response["name"]
        self.endpoint = endpoint
        self.header = {
            "Authorization": f"Bearer  {access_token}"
        }
        self.access_token = access_token

    def get(self, item_id):
        try:
            request = requests.get(self.endpoint+item_id, headers=self.header)
        except Exception as e:
            print(e)
        status = request.status_code
        if status != 200:
            print(request.text)
        response = request.json()
        return response


