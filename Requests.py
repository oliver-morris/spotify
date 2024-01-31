import requests
import json
from urllib.parse import quote

class Requests:
    def __init__(self, endpoints, access_token):
        self.access_token = access_token
        self.endpoints = endpoints
        self.header = {
            "Authorization": f"Bearer  {access_token}"
        }

    def get(self, endpoint, item_id):
        try:
            request = requests.get(endpoint+item_id, headers=self.header)
        except Exception as e:
            print(e)
        status = request.status_code
        if status != 200:
            print(status)
            print("Invalid Request")
            print(request.text)
        response = request.json()
        return response

    def getMultiple(self, endpoint, item_lists, max_size=20):
        items = []
        item_lists = [item_lists[x:x+max_size] for x in range(0, len(item_lists),max_size)]
        for item_list in item_lists:
            query_string = ""
            for item_id in item_list:
                query_string += str(item_id) + ","
            query_string = query_string[:-1]
            query_string = quote(query_string)
            r = self.get(endpoint, query_string)
            for item in list(r.values())[0]:
                if item:
                    items.append(item)
        return items