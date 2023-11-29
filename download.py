# https://storage.googleapis.com/42uz/express-backend/2%202%205.mp4 download video from url

import requests

url = "https://storage.googleapis.com/42uz/express-backend/2%202%205.mp4"
r = requests.get(url, stream=True)
with open("videos/42.mp4", "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

