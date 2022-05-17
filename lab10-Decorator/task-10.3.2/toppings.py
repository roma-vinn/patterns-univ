from beverages import Beverage
from abc import ABC


class BaseTopping(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage


class Milk(BaseTopping):
    def __init__(self, beverage: Beverage):
        super(Milk, self).__init__(beverage)

    def description(self) -> str:
        return self._beverage.description() + ' + milk'

    def cost(self) -> int:
        return self._beverage.cost() + 3


class Sugar(BaseTopping):
    def __init__(self, beverage: Beverage):
        super(Sugar, self).__init__(beverage)

    def description(self) -> str:
        return self._beverage.description() + ' + sugar'

    def cost(self) -> int:
        return self._beverage.cost() + 1


class SourCream(BaseTopping):
    def __init__(self, beverage: Beverage):
        super(SourCream, self).__init__(beverage)

    def description(self) -> str:
        return self._beverage.description() + ' + sour cream'

    def cost(self) -> int:
        return self._beverage.cost() + 3


class Cream(BaseTopping):
    def __init__(self, beverage: Beverage):
        super(Cream, self).__init__(beverage)

    def description(self) -> str:
        return self._beverage.description() + ' + cream'

    def cost(self) -> int:
        return self._beverage.cost() + 5
