from abc import ABC, abstractmethod
from .auto import Auto
from lab4.vehicle_calculator.calculators import CarCalculator, TruckCalculator
from lab4.vehicle_calculator.vehicles import Car, Truck


class Customs(ABC):
    @abstractmethod
    def vehicle_price(self, auto: Auto) -> float:
        pass

    @abstractmethod
    def tax(self, auto: Auto) -> float:
        pass


class Adapter(Customs):
    _usd2hrn = 29.4
    _price_hrn: float
    _truck_calc = TruckCalculator()
    _car_calc = CarCalculator()

    def vehicle_price(self, auto: Auto) -> float:
        if auto.model == 'truck':
            calc = self._truck_calc
            calc.set_vehicle(Truck(age=auto.age, mileage=auto.mileage))
        else:
            calc = self._car_calc
            calc.set_vehicle(Car(age=auto.age, model=auto.model, damage=1 if auto.damaged else 0))

        price_str = calc.calculate_price()
        price_usd = float(price_str[:-3])
        self._price_hrn = price_usd * self._usd2hrn
        return self._price_hrn

    def tax(self, auto: Auto) -> float:
        """Tax is 20% of the price"""
        return self.vehicle_price(auto) * 0.2


def test():
    autos = [
        Auto(age=2, model='truck', damaged=False, mileage=10000),
        Auto(age=10, model='Ford', damaged=True, mileage=500000),
        Auto(age=3, model='Tesla', damaged=False, mileage=75000),
    ]
    adapter = Adapter()
    for auto in autos:
        print(auto)
        print(f'Price: {adapter.vehicle_price(auto)}, tax: {adapter.tax(auto)}')
        print()


if __name__ == '__main__':
    test()
