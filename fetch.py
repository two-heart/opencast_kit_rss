import requests


def all_series():
    res = requests.get('https://opencast.informatik.kit.edu/search//series.json?limit=10000&offset=0&')
    return _inner_list(res.json())


def all_episodes(identifier):
    url = 'https://opencast.informatik.kit.edu/search/episode.json?limit=1000&offset=0&sid=' + identifier + '&'
    res = requests.get(url)
    return _inner_list(res.json())


def _inner_list(outer_json):
    return outer_json['search-results']['result']
