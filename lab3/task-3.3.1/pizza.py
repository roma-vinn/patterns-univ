from ingredients import Topping
from dough import Dough


class Pizza:
    def __init__(self, toppings: 'list[Topping]', dough: Dough):
        self._toppings = toppings
        self._dough = dough

    @property
    def cost(self):
        # pizza cost = dough cost + costs of toppings
        return self._dough.cost + sum([t.value for t in self._toppings])

    def __str__(self):
        return f"Pizza(dough={self._dough}," \
               f" toppings=[{', '.join([t.name for t in self._toppings])}])"

    def __repr__(self):
        return f"Pizza(dough={self._dough}," \
               f" toppings=[{', '.join([t.name for t in self._toppings])}])"
