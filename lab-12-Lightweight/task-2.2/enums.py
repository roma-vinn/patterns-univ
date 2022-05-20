from enum import Enum


class Fuel(Enum):
    Petrol = 0
    Diesel = 1
    Electric = 2


class Material(Enum):
    Steel = 0  # стальний диск
    Alloy = 1  # легкосплавний


class CarColor(Enum):
    White = 0
    Black = 1
    Red = 2
    Grey = 3


class CarType(Enum):
    Sedan = 0
    Hatchback = 1
    SUV = 2
