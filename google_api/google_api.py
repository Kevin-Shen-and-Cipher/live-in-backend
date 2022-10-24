import os
import string
import requests


class GoogleAPI(object):
    def __init__(self):
        self.google_map_api_key = os.environ.get('GOOGLE_MAP_API_KEY')

    def get_distance(self, coordinate1: string, coordinate2: string):
        url = self.__get_distance_url(coordinate1, coordinate2)
        response = requests.get(url).json()

        return float(response["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0])

    def get_coordinate(self, address):
        url = self.__get_coordinate_url()
        params = {'sensor': 'false', 'address': address}
        result = requests.get(url, params=params).json()[
            "results"][0]["geometry"]["location"]

        return result

    def __get_distance_url(self, coordinate1: string, coordinate2: string):
        return "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + coordinate1 + "&destinations=" + coordinate2+"&key=" + self.google_map_API_key

    def __get_coordinate_url(self):
        return 'https://maps.googleapis.com/maps/api/geocode/json?key=' + self.google_map_API_key
