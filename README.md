# Simple Spotify API Library

This library provides a simple interface for the Spotify API. The API has not been fully implemented but many of the important endpoints are included within this library as well as some additional features which could be of use such as getting all songs from a specific artist

---

**API Token**

You will need an client token and client secret to access the endpoints which you can get from (https://developer.spotify.com/documentation/web-api). Make sure to keep these secret and not include in any of your code.

---

**Example Usage**

```python
from spotify.Spotify import Spotify

spotify = Spotify(client_id, client_secret)

noah = spotify.search.artist("Noah Kahan")
taylor = spotify.get.artist("06HL4z0CvFAxyc27GXpf02")

tracks = taylor.getTracks()
print(tracks)
print(noah.genres)
```


These artist ids can be found by searching the artist or you can precode them for faster artist access and they can be found on the share artist links:

https://open.spotify.com/artist/4tuJ0bMpJh08umKkEXKUI5
