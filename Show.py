from Item import Item

class Show(Item):
    def __init__(self, access_token, response, endpoints):
        endpoint = endpoints["show"]
        super().__init__(access_token, endpoint, response, endpoints)
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
