from Item import Item

class Artist(Item):
    def __init__(self, access_token, response, endpoint):
        super().__init__(access_token, endpoint, response)
        self.albums = None
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
        endpoint = f"{self.endpoint}/{self.id}/albums"
        #i = self.artist.getReq()

