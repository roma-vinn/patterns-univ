from enums import CarType, CarColor
from car_parts import Engine, Wheel


class Car:
    def __init__(self, car_type: CarType, car_color: CarColor, engine: Engine, wheel: Wheel):
        self._car_type = car_type
        self._car_color = car_color
        self._engine = engine
        self._wheel = wheel

    def show_info(self):
        print(
            f'Car:\n'
            f'\ttype = {self._car_type}\n'
            f'\tcolor = {self._car_color}\n'
            f'\tengine = {self._engine}\n'
            f'\twheel = {self._wheel}'
        )
