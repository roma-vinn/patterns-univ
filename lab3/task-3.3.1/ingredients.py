from enum import Enum


class Flour(Enum):
    # values - price
    WHEAT = 10
    RYE = 14
    CORN = 16


class DoughType(Enum):
    # values - multipliers of cost
    SLIM = 0.8
    DEFAULT = 1
    CHEESY = 1.2


class Topping(Enum):
    TOMATO_PASTE = 6  # base

    CHEESE = 8
    OLIVES = 10
    SAUSAGE = 16
    PINEAPPLE = 10
    MEAT = 15
    TOMATO = 5
    BASIL = 4
    PEPERONI = 18
    MUSHROOMS = 8
