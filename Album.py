from Item import Item, ItemObject

class Album(Item):
    def __init__(self, access_token):
        endpoint = "https://api.spotify.com/v1/albums/"
        super().__init__(access_token, endpoint)

    def get(self, album_id):
        response = Item.get(self, album_id)
        return AlbumObject(response)


class AlbumObject(ItemObject):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)
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