from Auth import Auth
from Artist import Artist
from Album import Album
from Search import Search
from Track import Track
from Playlist import Playlist
from Episode import Episode
from AudioBook import AudioBook
from Show import Show

class Spotify:
    def __init__(self, client_id, client_secret):
        self.auth = Auth(client_id, client_secret)
        self.token = self.auth.getAccessToken()
        self.search = Search(self.token)
        self.artist = Artist(self.token)
        self.album = Album(self.token)
        self.track = Track(self.token)
        self.playlist = Playlist(self.token)
        #self.episode = Episode(self.token)
        self.audiobook = AudioBook(self.token)
        self.show = Show(self.token)