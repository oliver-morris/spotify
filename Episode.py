from Item import Item, ItemObject

class Episode(Item):
    def __init__(self, access_token):
        endpoint = "https://api.spotify.com/v1/episodes/"
        super().__init__(access_token, endpoint)

    def get(self, episode_id):
        response = Item.get(self, episode_id)
        return EpisodeObject(response)

class EpisodeObject(ItemObject):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)
        self.setAttributes()

    def setAttributes(self):
        self.preview_url = self.response["audio_preview_url"]
        self.description = self.response["description"]
        self.duration = self.response["duration_ms"]
        self.image = self.response["images"][0]["url"]
        self.languages = self.response["languages"]
        self.release_date = self.response["release_date"]

