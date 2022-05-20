from car import Car
from enums import CarType, CarColor, Fuel
from car_parts import Engine, Wheel


class CarBuilder:
    wheel_dict = {}
    engine_dict = {}

    def __init__(self):
        self._car_type: CarType = ...
        self._car_color: CarColor = ...
        self._engine: Engine = ...
        self._wheel: Wheel = ...

        self.reset()

    def reset(self):
        self._car_type = CarType.Sedan
        self._car_color = CarColor.White
        self._engine = Engine(105, Fuel.Petrol)
        self._wheel = Wheel(17)
        return self

    def set_car_type(self, car_type: CarType):
        self._car_type = car_type
        return self

    def set_car_color(self, car_color: CarColor):
        self._car_color = car_color
        return self

    def set_engine(self, engine: Engine):
        self._engine = engine
        return self

    def set_wheel(self, wheel: Wheel):
        self._wheel = wheel
        return self

    def build(self):
        return Car(
            car_type=self._car_type,
            car_color=self._car_color,
            engine=self._engine,
            wheel=self._wheel,
        )
