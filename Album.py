from Item import Item

class Album(Item):
    def __init__(self, access_token, response, endpoint):
        super().__init__(access_token, endpoint, response)
        self.setAttributes()

    def setAttributes(self):
        self.artists = {}
        self.tracks = {}
        for artist in self.response["artists"]:
            self.artists[artist["id"]] = artist["name"]
        for track in self.response["tracks"]["items"]:
            self.tracks[track["id"]] = track["name"]
        self.genres = self.response["genres"]
        self.album_cover = self.response["images"][0]["url"]
        self.label = self.response["label"]
        self.release_date = self.response["release_date"]
        self.popularity = self.response["popularity"]