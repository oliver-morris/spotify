import requests
import json
from urllib.parse import quote, unquote
from Artist import Artist
from Album import Album
from Track import Track
from Playlist import Playlist
from AudioBook import AudioBook
from Show import Show

class Search:
    def __init__(self, requests):
        self.requests = requests
        self.token = requests.access_token
        self.endpoint = "https://api.spotify.com/v1/search"
        self.header = {
            "Authorization": f"Bearer  {self.token}"
        }

    def request(self, search_query, type):
        search_query = quote(search_query)
        url = f"{self.endpoint}?q={search_query}&type={type}"
        try:
            request = requests.get(url, headers=self.header)
        except Exception as e:
            print(e)
        status = request.status_code
        if status != 200:
            print(request.text)
        response = request.json()
        items = response[f"{type}s"]["items"]
        if len(items) > 0:
            if items[0] != None:
                return items[0]
            else:
                print(f"{type}: {unquote(search_query)} not found!")
        else:
            print(f"{type}: {unquote(search_query)} not found!")


    def album(self, search_query):
        r = self.request(search_query, "album")
        if r:
            endpoint = self.requests.endpoints["album"]
            r = self.requests.get(endpoint, r["id"])
            return Album(r, self.requests)
    def artist(self, search_query):
        r = self.request(search_query, "artist")
        if r:
            return Artist(r, self.requests)
    def playlist(self, search_query):
        r = self.request(search_query, "playlist")
        if r:
            endpoint = self.requests.endpoints["playlist"]
            r = self.requests.get(endpoint, r["id"])
            return Playlist(r, self.requests)
    def track(self, search_query):
        r = self.request(search_query, "track")
        if r:
            return Track(r, self.requests)
    def show(self, search_query):
        r = self.request(search_query, "show")
        if r:
            endpoint = self.requests.endpoints["show"]
            r = self.requests.get(endpoint, r["id"])
            return Show(r, self.requests)
    def episode(self, search_query):
        r = self.request(search_query, "episode")
        if r:
            endpoint = self.requests.endpoints["episode"]
            r = self.requests.get.get(endpoint, r["id"])
            return Episode(r, self.requests)
    def audiobook(self, search_query):
        r = self.request(search_query, "audiobook")
        if r:
            endpoint = self.requests.endpoints["audiobook"]
            r = self.requests.get(endpoint, r["id"])
            return AudioBook(r, self.requests)
