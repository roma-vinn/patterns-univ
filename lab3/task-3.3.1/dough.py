from ingredients import DoughType, Flour


class Dough:
    def __init__(self, flour: Flour, dough_type: DoughType):
        self._flour = flour
        self._dough_type = dough_type

    @property
    def cost(self):
        # dough cost = dough type multiplier * flour cost
        return self._dough_type.value * self._flour.value

    def __str__(self):
        return f"Dough(flour={self._flour.name}, dough_type={self._dough_type.name})"

    def __repr__(self):
        return f"Dough(flour={self._flour.name}, dough_type={self._dough_type.name})"
