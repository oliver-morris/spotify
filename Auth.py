import requests
import json
import time

class Auth:
    def __init__(self, client_id, client_secret, endpoints):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_endpoint = endpoints["auth"]
        self.access_token, self.creation_time, self.expiry_time = self.auth()

    def auth(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        creation_time = time.time()
        try:
            request = requests.post(self.auth_endpoint, headers=header, data=body)
        except Exception as e:
            print(e)
        status = request.status_code
        if status != 200:
            print(request.text)
        response = request.json()
        access_token = response["access_token"]
        return access_token, creation_time, creation_time+response["expires_in"]

    def getAccessToken(self):
        return self.access_token