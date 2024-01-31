from Item import Item

class Playlist(Item):
    def __init__(self, access_token, response, endpoints):
        endpoint = endpoints["playlist"]
        super().__init__(access_token, endpoint, response, endpoints)
        self.setAttributes()

    def setAttributes(self):
        self.description = self.response["description"]
        self.followers = self.response["followers"]["total"]
        self.image = self.response["images"][0]["url"]
        self.owner = {self.response["owner"]["id"]:self.response["owner"]["display_name"]}
        self.tracks = {}
        for track in self.response["tracks"]["items"]:
            self.tracks[track["track"]["id"]] = track["track"]["name"]

