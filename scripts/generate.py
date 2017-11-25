import json
import requests

api_key = json.load(open("../json/api.json"))["key"]
list_url = "https://www.googleapis.com/youtube/v3/search?" \
      "part=snippet&channelId=UCwnKziETDbHJtx78nIkfYug&maxResults=50&pageToken={PT}&type=video&key={AK}"
info_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ID}&key={AK}"


def get_list(token=""):
    full_url = list_url
    if token:
        full_url = full_url.replace("{PT}", token)
    else:
        full_url = full_url.replace("&pageToken={PT}", "")
    return requests.get(full_url.replace("{AK}", api_key)).json()


def get_info(video_id):
    return requests.get(info_url.replace("{ID}", video_id).replace("{AK}", api_key)).json()


def generate():
    videos = {}
    result = get_list()
    add_to_dict(result["items"], videos)
    while "nextPageToken" in result:
        result = get_list(result["nextPageToken"])
        add_to_dict(result["items"], videos)
    return videos


def separate(videos):
    countries = json.load(open('../json/countries.json'))
    for video in videos:
        info = get_info(video)
        for country in countries:
            if country in info["items"][0]["snippet"]["tags"]:
                countries[country][video] = videos[video]
    with open('../json/countries.json', 'w') as outfile:
        json.dump(countries, outfile, indent=4)
    return


def clean_countries():
    countries = json.load(open('../json/countries.json'))
    for country in countries:
        countries[country] = {}
    with open('../json/countries.json', 'w') as outfile:
        json.dump(countries, outfile, indent=4)


def add_to_dict(begin, end):
    for video in begin:
        end[video["id"]["videoId"]] = video["snippet"]["title"]


if __name__ == "__main__":
    clean_countries()
    separate(generate())




