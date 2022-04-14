from abc import ABC, abstractmethod
from .vehicles import Vehicle


class VehicleCalculator(ABC):
    @abstractmethod
    def set_vehicle(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def calculate_price(self) -> str:
        pass


class TruckCalculator(VehicleCalculator):
    _vehicle: Vehicle
    _average_price = 6000

    def set_vehicle(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def calculate_price(self) -> str:
        assert self._vehicle is not None, "Must define vehicle before calculating its price"

        price = max(self.average_price - self._vehicle.age * 100 - self._vehicle.mileage / 100, 0)
        return f"{price}USD"

    @property
    def average_price(self):
        return self._average_price


class CarCalculator(VehicleCalculator):
    _vehicle: Vehicle
    _average_price = 6000

    def set_vehicle(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def _get_retail_price(self):
        assert self._vehicle is not None, "Must define vehicle before calculating its price"

        if self._vehicle.model == "Ford":
            return 3000
        elif self._vehicle.model == "Audi":
            return 5000
        elif self._vehicle.model == "BMW":
            return 7000
        elif self._vehicle.model == "Tesla":
            return 10000
        else:
            return self._average_price

    def calculate_price(self) -> str:
        assert self._vehicle is not None, "Must define vehicle before calculating its price"

        # original line was like this, but I suppose, it must be (1-damage) instead of damage
        # price = int(self._vehicle.damage * max(self._get_retail_price() - (self._vehicle.age * 100), 0))

        price = int((1 - self._vehicle.damage) * max(self._get_retail_price() - (self._vehicle.age * 100), 0))
        return f"{price}USD"

    @property
    def average_price(self):
        return self._average_price
