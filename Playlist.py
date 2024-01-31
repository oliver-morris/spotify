from Item import Item, ItemObject

class Playlist(Item):
    def __init__(self, access_token):
        endpoint = "https://api.spotify.com/v1/playlists/"
        super().__init__(access_token, endpoint)

    def get(self, playlist_id):
        response = Item.get(self, playlist_id)
        return PlaylistObject(response)

class PlaylistObject(ItemObject):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)
        self.setAttributes()

    def setAttributes(self):
        self.description = self.response["description"]
        self.followers = self.response["followers"]["total"]
        self.image = self.response["images"][0]["url"]
        self.owner = {self.response["owner"]["id"]:self.response["owner"]["display_name"]}
        self.tracks = {}
        for track in self.response["tracks"]["items"]:
            self.tracks[track["track"]["id"]] = track["track"]["name"]

