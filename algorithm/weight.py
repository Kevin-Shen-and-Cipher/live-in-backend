from abc import ABC, abstractmethod
import string


class Weight(ABC):
    def __init__(self) -> None:
        self.address = ""

    @abstractmethod
    def get_weight(self, item):
        return NotImplemented

    def sort(self, items: list, address: string):
        self.address = address

        items.sort(key=lambda item: self.get_weight(item))

        return items
