from Item import Item

class AudioBook(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["audiobook"]
        super().__init__(endpoint, response, requests)
        self.setAttributes()

    def setAttributes(self):
        self.authors = []
        for author in self.response["authors"]:
            self.authors.append(author["name"])
        self.narrators = []
        for narrator in self.response["narrators"]:
            self.narrators.append(narrator["name"])
        self.chapters = []
        for chapter in self.response["chapters"]["items"]:
            self.chapters.append(Chapter(chapter))
        self.publisher = self.response["publisher"]
        self.languages = self.response["languages"]
        self.description = self.response["description"]
        self.image = self.response["images"][0]["url"]


class Chapter:
    def __init__(self, chapter):
        self.id = chapter["id"]
        self.name = chapter["name"]
        self.description = chapter["description"]
        self.chapter_number = chapter["chapter_number"]
        self.image = chapter["images"][0]["url"]
        self.url = chapter["external_urls"]["spotify"]
        self.duration = chapter["duration_ms"]
        self.preview_url = chapter["audio_preview_url"]
        self.release_date = chapter["release_date"]
