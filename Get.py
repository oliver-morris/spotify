import requests
import json
from Album import Album
from Artist import Artist
from AudioBook import AudioBook
from Episode import Episode
from Playlist import Playlist
from Show import Show
from Track import Track


class Get:
    def __init__(self, access_token, endpoints):
        self.endpoints = endpoints
        self.access_token = access_token
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
            print(request.text)
        response = request.json()
        return response

    def album(self, album_id):
        endpoint = self.endpoints["album"]
        return Album(self.access_token, self.get(endpoint, album_id), endpoint)

    def artist(self, artist_id):
        endpoint = self.endpoints["artist"]
        return Artist(self.access_token, self.get(endpoint, artist_id), endpoint)

    def audiobook(self, audiobook_id):
        endpoint = self.endpoints["audiobook"]
        return AudioBook(self.access_token, self.get(endpoint, audiobook_id), endpoint)

    def episode(self, episode_id):
        endpoint = self.endpoints["episode"]
        return Episode(self.access_token, self.get(endpoint, episode_id), endpoint)

    def playlist(self, playlist_id):
        endpoint = self.endpoints["playlist"]
        return Playlist(self.access_token, self.get(endpoint, playlist_id), endpoint)

    def show(self, show_id):
        endpoint = self.endpoints["show"]
        return Show(self.access_token, self.get(endpoint, show_id), endpoint)

    def track(self, track_id):
        endpoint = self.endpoints["track"]
        return Track(self.access_token, self.get(endpoint, track_id), endpoint)