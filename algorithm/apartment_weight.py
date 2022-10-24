from algorithm.weight import Weight
from google_api.google_api import GoogleAPI


class ApartmentWeight(Weight):
    def get_weight(self, item):
        return 1