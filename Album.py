from Item import Item
from Track import Track

class Album(Item):
    def __init__(self, access_token, response, endpoints):
        endpoint = endpoints["album"]
        super().__init__(access_token, endpoint, response, endpoints)
        self.setAttributes()
        self.tracks = []

    def setAttributes(self):
        self.artists = {}
        #self.tracks = {}
        for artist in self.response["artists"]:
            self.artists[artist["id"]] = artist["name"]
        #for track in self.response["tracks"]["items"]:
        #    self.tracks[track["id"]] = track["name"]
        self.genres = self.response["genres"]
        self.album_cover = self.response["images"][0]["url"]
        self.label = self.response["label"]
        self.release_date = self.response["release_date"]
        self.popularity = self.response["popularity"]

    def getTracks(self, from_memory=True):
        if from_memory:
            if self.tracks:
                return self.tracks
        endpoint_search = f"{self.id}/tracks"
        r = Item.get(self, endpoint_search)
        self.tracks = []
        for track in r["items"]:
            id = track["id"]
            r = Item.get(self, id, self.endpoints["track"])
            self.tracks.append(Track(self.access_token, r, self.endpoints))
        return self.tracks