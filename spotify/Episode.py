from .Item import Item

class Episode(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["episode"]
        super().__init__(endpoint, response, requests)
        self.setAttributes()

    def setAttributes(self):
        self.preview_url = self.response["audio_preview_url"]
        self.description = self.response["description"]
        self.duration = self.response["duration_ms"]
        self.image = self.response["images"][0]["url"]
        self.languages = self.response["languages"]
        self.release_date = self.response["release_date"]

