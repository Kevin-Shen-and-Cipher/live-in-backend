import requests

google_map_API_key = "YOUR API KEY"
def get_corrd(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + google_map_API_key
    params = {'sensor': 'false', 'address': address}
    r = requests.get(url, params=params).json()["results"][0]["geometry"]["location"]
    return r