from .Item import Item
from .ItemList import ItemList
from .Track import Track

class Album(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["album"]
        super().__init__(endpoint, response, requests)
        self.setAttributes()
        self.tracks = ItemList([])

    def setAttributes(self):
        self.artists = {}
        for artist in self.response["artists"]:
            self.artists[artist["id"]] = artist["name"]
        self.genres = self.response["genres"]
        self.album_cover = self.response["images"][0]["url"]
        self.label = self.response["label"]
        self.release_date = self.response["release_date"]
        self.popularity = self.response["popularity"]

    def getTracks(self, from_memory=True):
        if from_memory:
            if self.tracks.items:
                return self.tracks
        endpoint_search = f"{self.id}/tracks"
        r = Item.get(self, endpoint_search)
        self.tracks = ItemList([])
        ids = []
        for track in r["items"]:
            ids.append(track["id"])
        endpoint = self.requests.endpoints["several_tracks"]
        r = self.requests.getMultiple(endpoint, ids)
        for track in r:
            if track:
                track_id = track["id"]
                if track_id not in self.tracks.ids():
                    track = Track(track, self.requests)
                    self.tracks.add(track)
        return self.tracks