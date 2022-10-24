import os
import string
import requests


class GoogleAPI(object):
    def __init__(self):
        self.google_map_api_key = os.environ.get('GOOGLE_MAP_API_KEY')

    def get_distance(self, coordinate1: string, coordinate2: string):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        params = {
            'origins': coordinate1,
            'destinations': coordinate2,
            'key': self.google_map_api_key
        }

        response = requests.get(url, params=params).json()

        result = float(response["rows"][0]["elements"][0]["distance"]['value'])

        return result

    def get_coordinate(self, address: string):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'sensor': 'false',
            'address': address,
            'key': self.google_map_api_key
        }

        response = requests.get(url, params=params).json()
        coordinate = response["results"][0]["geometry"]["location"]

        result = ','.join(str(val) for val in coordinate.values())

        return result
