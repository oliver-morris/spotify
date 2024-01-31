import requests
import json
from urllib.parse import quote, unquote
from Artist import Artist, ArtistObject
from Album import Album
from Track import Track, TrackObject
from Playlist import Playlist
from AudioBook import AudioBook
from Show import Show

class Search:
    def __init__(self, access_token):
        self.token = access_token
        self.endpoint = "https://api.spotify.com/v1/search"
        self.header = {
            "Authorization": f"Bearer  {self.token}"
        }
        self.artist_obj = Artist(self.token)
        self.album_obj = Album(self.token)
        self.track_obj = Track(self.token)
        self.playlist_obj = Playlist(self.token)
        #self.episode_obj = Episode(self.token)
        self.audiobook_obj = AudioBook(self.token)
        self.show_obj = Show(self.token)

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
            return self.album_obj.get(r["id"])
    def artist(self, search_query):
        r = self.request(search_query, "artist")
        if r:
            return ArtistObject(self.token, r)
    def playlist(self, search_query):
        r = self.request(search_query, "playlist")
        if r:
            return self.playlist_obj.get(r["id"])
    def track(self, search_query):
        r = self.request(search_query, "track")
        if r:
            return TrackObject(r)
    def show(self, search_query):
        r = self.request(search_query, "show")
        if r:
            return self.show_obj.get(r["id"])
    def episode(self, search_query):
        r = self.request(search_query, "episode")
    def audiobook(self, search_query):
        r = self.request(search_query, "audiobook")
        if r:
            return self.audiobook_obj.get(r["id"])
