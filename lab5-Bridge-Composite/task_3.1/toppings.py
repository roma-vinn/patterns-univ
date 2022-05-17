from abc import ABC, abstractmethod


class Topping(ABC):
    name: str
    measurement_unit: str

    @abstractmethod
    def added_value(self) -> int:
        pass

    @abstractmethod
    def prepare(self):
        pass

    def _prepare(self, topping_value):
        print(f'\tPutting some {self.name}: {topping_value}{self.measurement_unit}')

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def measurement_unit(self):
        pass


class Milk(Topping):
    def __init__(self, milk_volume: int):
        self._milk_volume = milk_volume

    def prepare(self):
        super(Milk, self)._prepare(self._milk_volume)

    def added_value(self) -> int:
        return int(self._milk_volume / 20)

    @property
    def name(self):
        return 'milk'

    @property
    def measurement_unit(self):
        return 'ml'


class ExtraHotWater(Topping):
    def __init__(self, water_volume: int):
        self._water_volume = water_volume

    def added_value(self) -> int:
        return 0

    def prepare(self):
        super(ExtraHotWater, self)._prepare(self._water_volume)

    @property
    def name(self):
        return 'extra hot water'

    @property
    def measurement_unit(self):
        return 'ml'


class ExtraCoffee(Topping):
    def __init__(self, extra_coffee: int):
        self._extra_coffee = extra_coffee

    def added_value(self) -> int:
        return 5 * self._extra_coffee

    def prepare(self):
        super(ExtraCoffee, self)._prepare(self._extra_coffee)

    @property
    def name(self):
        return 'extra coffee'

    @property
    def measurement_unit(self):
        return 'portion'
