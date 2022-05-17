from ingredients import DoughType, Flour, Topping
from pizza import Pizza
from dough import Dough


class PizzaBuilder:
    _flour: Flour
    _dough_type: DoughType
    _toppings: 'list[Topping]'

    def __init__(self):
        self.reset()

    def reset(self):
        self._flour = Flour.WHEAT
        self._dough_type = DoughType.DEFAULT
        self._toppings = [Topping.TOMATO_PASTE]

        return self

    def set_flour(self, flour: Flour):
        assert isinstance(flour, Flour), \
            f'flour must be instance of class Flour, got: {type(flour)}'

        self._flour = flour
        return self

    def set_dough_type(self, dough_type: DoughType):
        assert isinstance(dough_type, DoughType), \
            f'dough_type must be instance of class Topping, got: {type(dough_type)}'

        self._dough_type = dough_type
        return self

    def add_topping(self, topping: Topping):
        assert isinstance(topping, Topping),\
            f'topping must be instance of class Topping, got: {type(topping)}'

        self._toppings.append(topping)
        return self

    def build(self):
        if self._dough_type is None or self._flour is None or self._toppings is None:
            raise ValueError('Incorrect pizza parameters.')

        return Pizza(
            toppings=self._toppings,
            dough=Dough(dough_type=self._dough_type, flour=self._flour)
        )
