import requests
import json


def instagram_download(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {
        "url": link
    }

    headers = {
        "X-RapidAPI-Key": "a53b6d314emsh82f24f317bc95e6p1b3e8bjsnb431799397a9",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        result = {}
        if rest['Type'] == "Post-Image":
            result['type'] = 'image'
            result['media'] = rest['media']
            return result
        elif rest['Type'] == "Post-Video":
            result['type'] = 'video'
            result['media'] = rest['media']
            return result
        elif rest['Type'] == 'Carousel':
            result['type'] = 'carousel'
            result['media'] = rest['media']
            return result
        else:
            return 'Bad'
