from Item import Item, ItemObject

class Artist(Item):
    def __init__(self, access_token):
        endpoint = "https://api.spotify.com/v1/artists/"
        super().__init__(access_token, endpoint)

    def get(self, artist_id):
        response = Item.get(self, artist_id)
        return ArtistObject(self.token, response)


class ArtistObject(ItemObject):
    def __init__(self, token, response):
        self.response = response
        self.token = token
        self.albums = None
        super().__init__(self.response)
        self.setAttributes()

    def setAttributes(self):
        self.followers = self.response["followers"]["total"]
        self.genres = self.response["genres"]
        self.profile_picture = self.response["images"][0]["url"]
        self.popularity = self.response["popularity"]

    def getAlbums(self, from_memory=False):
        if from_memory:
            if self.albums:
                return self.albums
        endpoint = f"https://api.spotify.com/v1/artists/{self.id}/albums"

