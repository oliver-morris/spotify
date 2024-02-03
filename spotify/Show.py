from .Item import Item

class Show(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["show"]
        super().__init__(endpoint, response, requests)
        self.albums = None
        self.setAttributes()

    def setAttributes(self):
        self.episodes = []
        for episode in self.response["episodes"]["items"]:
            self.episodes.append(EpisodeObject(episode))
        self.description = self.response["description"]
        self.image = self.response["images"][0]["url"]
        self.languages = self.response["languages"]
        self.publisher = self.response["publisher"]
