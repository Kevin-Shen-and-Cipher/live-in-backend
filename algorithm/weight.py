import string
from abc import ABC, abstractmethod

from google_api.google_api import GoogleAPI


class Weight(ABC):
    def __init__(self) -> None:
        self.address = ""
        self.google_api = GoogleAPI()

    @abstractmethod
    def get_weight(self, item):
        return NotImplemented

    def sort(self, items: list, address: string):
        self.address = address

        items.sort(key=lambda item: self.get_weight(item), reverse=True)

        return items
