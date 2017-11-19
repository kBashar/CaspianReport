import json
import requests

api_key = json.load(open("../json/api.json"))["key"]
api_url = "https://www.googleapis.com/youtube/v3/search?" \
      "part=snippet&channelId=UCwnKziETDbHJtx78nIkfYug&maxResults=50&pageToken={PT}&type=video&key={AK}"


def get_list(token=""):
    full_url = api_url
    if token:
        full_url = full_url.replace("{PT}", token)
    else:
        full_url = full_url.replace("&pageToken={PT}", "")
    return requests.get(full_url.replace("{AK}", api_key)).json()


def generate():
    videos = {}
    result = get_list()
    add_to_dict(result["items"], videos)
    while "nextPageToken" in result:
        result = get_list(result["nextPageToken"])
        add_to_dict(result["items"], videos)
    return videos


def add_to_dict(begin, end):
    for video in begin:
        end[video["id"]["videoId"]] = video["snippet"]["title"]


if __name__ == "__main__":
    print(api_key)
    with open('../json/videos.json', 'w') as fp:
        json.dump(generate(), fp, indent=4)


