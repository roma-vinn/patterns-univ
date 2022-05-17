class Vehicle:
    def __init__(self, age: int = 0, model: str = "default", damage: float = 0, mileage: int = 0):
        self._age = age
        self._model = model
        self._damage = damage  # 0 - no damage, 1 - completely damaged
        self._mileage = mileage

    @property
    def age(self):
        return self._age

    @property
    def model(self):
        return self._model

    @property
    def damage(self):
        return self._damage

    @property
    def mileage(self):
        return self._mileage


class Car(Vehicle):
    def __init__(self, age: int, model: str, damage: float):
        super(Car, self).__init__(age=age, model=model, damage=damage, mileage=0)


class Truck(Vehicle):
    def __init__(self, age: int, mileage: int):
        super(Truck, self).__init__(age=age, model='truck', damage=0, mileage=mileage)
