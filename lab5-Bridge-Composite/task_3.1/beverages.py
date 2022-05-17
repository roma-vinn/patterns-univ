from abc import ABC, abstractmethod
from toppings import Topping
from servings import Serving


class Beverage(ABC):
    def __init__(self, sugar: int, topping: Topping = None, serving: Serving = None):
        self._sugar = sugar
        self._topping = topping
        self._serving = serving

    @abstractmethod
    def prepare(self):
        pass

    def drink(self):
        with_str = ' with ' + self._topping.name if self._topping is not None else ''
        if self._serving is None:
            print(f'Drinking {self.name}{with_str} in cafe')
        else:
            print(f'Taking {self.name}{with_str} as {str(self._serving)}')

    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Tea(Beverage):
    def __init__(self, sugar: int = 0, topping: Topping = None, serving: Serving = None):
        super(Tea, self).__init__(sugar, topping, serving)

    def prepare(self):
        print('Preparing:')
        print('\tPouring some tea')
        if self._topping is not None:
            self._topping.prepare()
        if self._sugar > 0:
            print(f'\tAdding sugar: {self._sugar} pieces')

    def cost(self) -> int:
        top_value = self._topping.added_value() if self._topping is not None else 0
        serv_value = self._serving.added_value() if self._serving is not None else 0
        return 7 + top_value + serv_value

    @property
    def name(self):
        return 'tea'


class Coffee(Beverage):
    def __init__(self, sugar: int = 0, topping: Topping = None, serving: Serving = None):
        super(Coffee, self).__init__(sugar, topping, serving)

    def prepare(self):
        print('Preparing:')
        print('\tPouring some coffee')
        if self._topping is not None:
            self._topping.prepare()
        if self._sugar > 0:
            print(f'\tAdding sugar: {self._sugar} pieces')

    def cost(self) -> int:
        top_value = self._topping.added_value() if self._topping is not None else 0
        serv_value = self._serving.added_value() if self._serving is not None else 0
        return 10 + top_value + serv_value

    @property
    def name(self):
        return 'coffee'


class Chocolate(Beverage):
    def __init__(self, sugar: int = 0, topping: Topping = None, serving: Serving = None):
        super(Chocolate, self).__init__(sugar, topping, serving)

    def prepare(self):
        print('Preparing:')
        print('\tPouring some chocolate')
        if self._topping is not None:
            self._topping.prepare()
        if self._sugar > 0:
            print(f'\tAdding sugar: {self._sugar} pieces')

    def cost(self) -> int:
        top_value = self._topping.added_value() if self._topping is not None else 0
        serv_value = self._serving.added_value() if self._serving is not None else 0
        return 15 + top_value + serv_value

    @property
    def name(self):
        return 'chocolate'
