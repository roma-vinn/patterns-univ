from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> int:
        pass


class Espresso(Beverage):
    def description(self):
        return 'Espresso'

    def cost(self) -> int:
        return 12


class DarkRoast(Beverage):
    def description(self) -> str:
        return 'Dark Roast'

    def cost(self) -> int:
        return 9


class Decaf(Beverage):
    def description(self) -> str:
        return 'Decaf'

    def cost(self) -> int:
        return 18
