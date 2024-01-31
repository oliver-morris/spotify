from Item import Item
from Album import Album
from ItemList import ItemList

class Artist(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["artist"]
        super().__init__(endpoint, response, requests)
        self.albums = ItemList([])
        self.tracks = ItemList([])
        self.setAttributes()

    def setAttributes(self):
        self.followers = self.response["followers"]["total"]
        self.genres = self.response["genres"]
        self.profile_picture = self.response["images"][0]["url"]
        self.popularity = self.response["popularity"]

    def getAlbums(self, from_memory=True):
        if from_memory:
            if self.albums.items:
                return self.albums
        endpoint_search = f"{self.id}/albums"
        r = Item.get(self, endpoint_search)
        self.albums = ItemList([])
        ids = []
        for album in r["items"]:
            ids.append(album["id"])
        endpoint = self.requests.endpoints["several_albums"]
        r = self.requests.getMultiple(endpoint, ids)
        for album in r:
            if album:
                album_id = album["id"]
                if album_id not in self.albums.ids():
                    album = Album(album, self.requests)
                    self.albums.add(album)
        return self.albums

    def getTracks(self, from_memory=True):
        if from_memory:
            if self.tracks.items:
                return self.tracks
        albums = self.getAlbums(from_memory)
        self.tracks = ItemList([])
        for album in albums.items:
            tracks = album.getTracks(from_memory)
            for track in tracks.items:
                if track.id not in self.tracks.ids():
                    self.tracks.add(track)
        return self.tracks



