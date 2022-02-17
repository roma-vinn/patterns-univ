from abc import ABC, abstractmethod
from drinks import Drink, Espresso, Americano, Cappuccino, Latte, Cocoa


class Cooker(ABC):  # Creator
    @abstractmethod
    def cook(self) -> Drink:
        pass


class EspressoCooker(Cooker):  # Concrete creator
    def cook(self) -> Espresso:
        return Espresso()


class AmericanoCooker(Cooker):  # Concrete creator
    def cook(self) -> Americano:
        return Americano()


class CappuccinoCooker(Cooker):  # Concrete creator
    def cook(self) -> Cappuccino:
        return Cappuccino()


class LatteCooker(Cooker):  # Concrete creator
    def cook(self) -> Latte:
        return Latte()


class CocoaCooker(Cooker):  # Concrete creator
    def cook(self) -> Cocoa:
        return Cocoa()
