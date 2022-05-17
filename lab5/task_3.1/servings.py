from abc import ABC, abstractmethod


class Serving(ABC):
    @abstractmethod
    def added_value(self) -> int:
        pass

    @abstractmethod
    def __str__(self):
        pass


class TakeOut(Serving):
    def added_value(self) -> int:
        return 3  # price of a cup

    def __str__(self):
        return 'take-out'


class Delivery(Serving):
    def __init__(self, address: str):
        self._address = address

    def added_value(self) -> int:
        return 40  # price of a delivery

    def __str__(self):
        return f'delivery to {self._address}'
