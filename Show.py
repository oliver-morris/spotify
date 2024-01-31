from Item import Item, ItemObject
from Episode import EpisodeObject

class Show(Item):
    def __init__(self, access_token):
        endpoint = "https://api.spotify.com/v1/shows/"
        super().__init__(access_token, endpoint)

    def get(self, show_id):
        response = Item.get(self, show_id)
        return ShowObject(response)

class ShowObject(ItemObject):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)
        self.setAttributes()

    def setAttributes(self):
        self.episodes = []
        for episode in self.response["episodes"]["items"]:
            self.episodes.append(EpisodeObject(episode))
        self.description = self.response["description"]
        self.image = self.response["images"][0]["url"]
        self.languages = self.response["languages"]
        self.publisher = self.response["publisher"]
