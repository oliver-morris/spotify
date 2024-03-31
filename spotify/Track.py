from .Item import Item
import os
import string
from urllib.parse import quote
import requests
from pytube import YouTube

class Track(Item):
    def __init__(self, response, requests):
        endpoint = requests.endpoints["track"]
        super().__init__(endpoint, response, requests)
        self.setAttributes()

    def setAttributes(self):
        self.album = {self.response["album"]["id"]:self.response["album"]["name"]}
        self.artists = {}
        for artist in self.response["artists"]:
            self.artists[artist["id"]] = artist["name"]
        self.preview_url = self.response["preview_url"]
        self.track_number = self.response["track_number"]
        self.popularity = self.response["popularity"]

    def download(self, path=None, file_name=None):
        if not file_name:
            file_name = f"video_{self.id}.mp4"
        file_path = ""
        artist_name = list(self.artists.values())[0]
        if path:
            if ":" in path:
                file_path = path
            else:
                abs_path = os.path.abspath(os.path.dirname(__file__))
                file_path = abs_path
                path = path.replace("/", "\\")
                print(path[0])
                if path[0] != "\\":
                    file_path += "\\"
                file_path += path
        else:
            artist_id = list(self.artists.keys())[0]
            file_path = artist_name + " " + artist_id
            translator = str.maketrans(string.punctuation, '_'*len(string.punctuation))
            file_path = file_path.translate(translator)
            file_path = file_path.replace(" ", "_")
            abs_path = os.path.abspath(os.path.dirname(__file__))
            file_path = f"{abs_path}\\videos\\{file_path}"

        youtube_search_query = f"{self.name} - {artist_name} lyric video"
        youtube_search_query = quote(youtube_search_query)

        youtube_search_endpoint = f"https://www.youtube.com/results?search_query={youtube_search_query}"
        request = requests.get(youtube_search_endpoint)
        status = request.status_code
        if status == 200:
            response = request.text
            video_id = response.split('{"videoRenderer":{"videoId":"')[1]
            video_id = video_id.split('"')[0]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            #try:
            yt = YouTube(video_url)
            #except:
                #print("Connection Error")
            yt.streams.filter(progressive=True,
                                  file_extension="mp4").first().download(
                    output_path=file_path,
                    filename=file_name)
            return file_path + "\\" + file_name

    def getEmbed(self):
        return f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{self.id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'
