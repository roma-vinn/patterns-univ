from abc import ABC
from ingredients import Ingredients


class Drink(ABC):  # Product
    def __init__(self, ingredients: 'list[Ingredients]', cooking_cost: float):
        self._ingredients = ingredients
        self._cooking_cost = cooking_cost

    @property
    def cost(self):
        return sum([i.value for i in self._ingredients]) + self._cooking_cost

    @property
    def ingredients_list(self):
        return self._ingredients


class Espresso(Drink):  # Concrete product
    def __init__(self):
        super().__init__([Ingredients.WATER, Ingredients.COFFEE], cooking_cost=2)


class Americano(Drink):  # Concrete product
    def __init__(self):
        super().__init__([Ingredients.WATER, Ingredients.WATER, Ingredients.COFFEE], cooking_cost=3)


class Cappuccino(Drink):  # Concrete product
    def __init__(self):
        super().__init__(
            [Ingredients.WATER, Ingredients.COFFEE, Ingredients.MILK, Ingredients.MILK_FOAM],
            cooking_cost=4
        )


class Latte(Drink):  # Concrete product
    def __init__(self):
        super().__init__(
            [Ingredients.WATER, Ingredients.COFFEE, Ingredients.MILK, Ingredients.MILK_FOAM, Ingredients.MILK_FOAM],
            cooking_cost=6
        )


class Cocoa(Drink):  # Concrete product
    def __init__(self):
        super(Cocoa, self).__init__(
            [Ingredients.WATER, Ingredients.MILK, Ingredients.COCOA],
            cooking_cost=4
        )
