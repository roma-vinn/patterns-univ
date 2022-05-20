from enums import Fuel, Material


class Engine:
    cached = {}

    def __init__(self, power: int, fuel: Fuel):
        self._power = power
        self._fuel = fuel

    def __str__(self):
        return f"Engine(power={self._power}, fuel={self._fuel})"


class EngineBuilder:
    def __init__(self):
        self._cached = {}

        self._power = ...
        self._fuel = ...

    def reset(self):
        self._power = 105
        self._fuel = Fuel.Petrol
        return self

    def set_power(self, power: int):
        self._power = power
        return self

    def set_fuel(self, fuel: Fuel):
        self._fuel = fuel
        return self

    def build(self, power: int, fuel: Fuel):
        if (power, fuel) in self._cached:
            engine = self._cached.get((power, fuel))
            print(f'Cached {engine}')
        else:
            engine = Engine(power, fuel)
            self._cached[(power, fuel)] = engine
            print(f'New {engine}')
        return engine


class Wheel:
    cached = {}

    def __init__(self, diameter: int, material: Material = Material.Alloy):
        self._diameter = diameter
        self._material = material

    def __str__(self):
        return f"Wheel(diameter={self._diameter}, material={self._material})"


class WheelBuilder:
    def __init__(self):
        self._cached = {}

        self._diameter = ...
        self._material = ...

    def reset(self):
        self._diameter = 17
        self._material = Material.Alloy
        return self

    def set_diameter(self, diameter: int):
        self._diameter = diameter
        return self

    def set_material(self, material: Material):
        self._material = material
        return self

    def build(self, diameter: int, material: Material):
        if (diameter, material) in self._cached:
            wheel = self._cached.get((diameter, material))
            print(f'Cached {wheel}')
        else:
            wheel = Wheel(diameter, material)
            self._cached[(diameter, material)] = wheel
            print(f'New {wheel}')
        return wheel
