from Item import Item
from Album import Album

class Artist(Item):
    def __init__(self, access_token, response, endpoints):
        endpoint = endpoints["artist"]
        super().__init__(access_token, endpoint, response, endpoints)
        self.albums = []
        self.setAttributes()

    def setAttributes(self):
        self.followers = self.response["followers"]["total"]
        self.genres = self.response["genres"]
        self.profile_picture = self.response["images"][0]["url"]
        self.popularity = self.response["popularity"]

    def getAlbums(self, from_memory=True):
        if from_memory:
            if self.albums:
                return self.albums
        endpoint_search = f"{self.id}/albums"
        r = Item.get(self, endpoint_search)
        self.albums = []
        for album in r["items"]:
            id = album["id"]
            r = Item.get(self, id, self.endpoints["album"])
            self.albums.append(Album(self.access_token, r, self.endpoints))
        return self.albums


