from pizza_builder import PizzaBuilder
from common.singletone import Singleton
from ingredients import Topping, Flour
from dough import DoughType


class Pizzaiolo(metaclass=Singleton):
    _pizza_builder: PizzaBuilder

    def set_pizza_builder(self, pizza_builder: PizzaBuilder):
        assert isinstance(pizza_builder, PizzaBuilder), \
            'pizza_builder must be instance of class PizzaBuilder,' \
            f' got: {type(pizza_builder)}'

        self._pizza_builder = pizza_builder

    def _check_builder(self):
        assert self._pizza_builder is not None, \
            'you need to set pizza builder before cooking'

    def cook_Margarita(self):
        self._check_builder()

        return self._pizza_builder \
            .reset() \
            .add_topping(Topping.BASIL) \
            .add_topping(Topping.CHEESE) \
            .add_topping(Topping.TOMATO) \
            .build()

    def cook_Peperoni(self):
        self._check_builder()

        return self._pizza_builder \
            .reset() \
            .set_dough_type(DoughType.SLIM) \
            .add_topping(Topping.CHEESE) \
            .add_topping(Topping.TOMATO) \
            .add_topping(Topping.PEPERONI) \
            .build()

    def cook_Hawaiian(self):
        self._check_builder()

        return self._pizza_builder \
            .reset() \
            .set_flour(Flour.CORN) \
            .add_topping(Topping.MEAT) \
            .add_topping(Topping.PINEAPPLE) \
            .add_topping(Topping.CHEESE) \
            .build()
