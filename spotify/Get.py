import json
from urllib.parse import quote
from .Album import Album
from .Artist import Artist
from .AudioBook import AudioBook
from .Episode import Episode
from .Playlist import Playlist
from .Show import Show
from .Track import Track
from .Requests import Requests


class Get:
    def __init__(self, requests):
        self.requests = requests
        self.endpoints = requests.endpoints
        self.access_token = requests.access_token

    def get(self, endpoint, item_id):
        return self.requests.get(endpoint, item_id)

    def album(self, album_id):
        endpoint = self.endpoints["album"]
        if type(album_id) == list:
            albums = []
            endpoint = self.endpoints["several_albums"]
            r = self.requests.getMultiple(endpoint, album_id)
            for album in r:
                if album:
                    album_id = album["id"]
                    album = Album(album, self.requests)
                    albums.append(album)
            return albums
        return Album(self.requests.get(endpoint, album_id), self.requests)

    def artist(self, artist_id):
        endpoint = self.endpoints["artist"]
        if type(artist_id) == list:
            artists = []
            endpoint = self.endpoints["several_artists"]
            r = self.requests.getMultiple(endpoint, artist_id)
            for artist in r:
                if artist:
                    artist_id = artist["id"]
                    artist = Artist(artist, self.requests)
                    artists.append(artist)
            return artists
        return Artist(self.requests.get(endpoint, artist_id), self.requests)

    def audiobook(self, audiobook_id):
        endpoint = self.endpoints["audiobook"]
        if type(audiobook_id) == list:
            audiobooks = []
            endpoint = self.endpoints["several_audiobooks"]
            r = self.requests.getMultiple(endpoint, audiobook_id)
            for audiobook in r:
                if audiobook:
                    audiobook_id = audiobook["id"]
                    audiobook = AudioBook(audiobook, self.requests)
                    audiobooks.append(audiobook)
            return audiobooks
        return AudioBook(self.requests.get(endpoint, audiobook_id), self.requests)

    def episode(self, episode_id):
        endpoint = self.endpoints["episode"]
        if type(episode_id) == list:
            episodes = []
            endpoint = self.endpoints["several_episodes"]
            r = self.requests.getMultiple(endpoint, episode_id)
            for episode in r:
                if episode:
                    episode_id = episode["id"]
                    episode = Episode(episode, self.requests)
                    episodes.append(episode)
            return episodes
        return Episode(self.requests.get(endpoint, episode_id), self.requests)

    def playlist(self, playlist_id):
        endpoint = self.endpoints["playlist"]
        if type(playlist_id) == list:
            playlists = []
            for playlist in playlist_id:
                r = self.requests.get(endpoint, playlist)
                if r:
                    p = Playlist(r, self.requests)
                    if p:
                        playlists.append(p)
            return playlists
        return Playlist(self.requests.get(endpoint, playlist_id), self.requests)

    def show(self, show_id):
        endpoint = self.endpoints["show"]
        if type(show_id) == list:
            shows = []
            endpoint = self.endpoints["several_shows"]
            r = self.requests.getMultiple(endpoint, show_id)
            for show in r:
                if show:
                    show_id = show["id"]
                    show = Show(show, self.requests)
                    shows.append(show)
            return shows
        return Show(self.requests.get(endpoint, show_id), self.requests)

    def track(self, track_id):
        endpoint = self.endpoints["track"]
        if type(track_id) == list:
            tracks = []
            endpoint = self.endpoints["several_tracks"]
            r = self.requests.getMultiple(endpoint, track_id)
            for track in r:
                if track:
                    track_id = track["id"]
                    track = Track(track, self.requests)
                    tracks.append(track)
            return tracks
        return Track(self.requests.get(endpoint, track_id), self.requests)