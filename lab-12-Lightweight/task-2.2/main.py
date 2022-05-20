from random import randint, choice
from enums import Fuel, CarColor, CarType, Material
from car_builder import CarBuilder
from car_parts import EngineBuilder, WheelBuilder
from time import sleep


def create_random_car(
        car_builder: CarBuilder, engine_builder: EngineBuilder, wheel_builder: WheelBuilder, vehicles: list
):
    # >>> here is lightweight logic
    engine = engine_builder.build(power=randint(11, 15) * 10, fuel=choice(list(Fuel)))
    wheel = wheel_builder.build(diameter=randint(17, 20), material=Material.Alloy)
    # <<<

    car = car_builder.reset().\
        set_car_color(choice(list(CarColor))).\
        set_car_type(choice(list(CarType))).\
        set_engine(engine).\
        set_wheel(wheel)\
        .build()

    car.show_info()
    print()

    vehicles.append(car)


def main():
    car_builder = CarBuilder()
    engine_builder = EngineBuilder()
    wheel_builder = WheelBuilder()
    vehicles = []

    while True:
        create_random_car(car_builder, engine_builder, wheel_builder, vehicles)
        sleep(1)


if __name__ == '__main__':
    main()
    # New Engine(power=130, fuel=Fuel.Diesel)
    # New Wheel(diameter=19, material=Material.Alloy)
    # Car:
    # 	type = CarType.Sedan
    # 	color = CarColor.Grey
    # 	engine = Engine(power=130, fuel=Fuel.Diesel)
    # 	wheel = Wheel(diameter=19, material=Material.Alloy)
    #
    # Cached Engine(power=130, fuel=Fuel.Diesel)
    # New Wheel(diameter=17, material=Material.Alloy)
    # Car:
    # 	type = CarType.SUV
    # 	color = CarColor.Red
    # 	engine = Engine(power=130, fuel=Fuel.Diesel)
    # 	wheel = Wheel(diameter=17, material=Material.Alloy)
    #
    # New Engine(power=150, fuel=Fuel.Petrol)
    # New Wheel(diameter=18, material=Material.Alloy)
    # Car:
    # 	type = CarType.SUV
    # 	color = CarColor.Red
    # 	engine = Engine(power=150, fuel=Fuel.Petrol)
    # 	wheel = Wheel(diameter=18, material=Material.Alloy)
    #
    # New Engine(power=110, fuel=Fuel.Petrol)
    # Cached Wheel(diameter=17, material=Material.Alloy)
    # Car:
    # 	type = CarType.Hatchback
    # 	color = CarColor.Red
    # 	engine = Engine(power=110, fuel=Fuel.Petrol)
    # 	wheel = Wheel(diameter=17, material=Material.Alloy)
    #
    # New Engine(power=130, fuel=Fuel.Petrol)
    # Cached Wheel(diameter=18, material=Material.Alloy)
    # Car:
    # 	type = CarType.Sedan
    # 	color = CarColor.Black
    # 	engine = Engine(power=130, fuel=Fuel.Petrol)
    # 	wheel = Wheel(diameter=18, material=Material.Alloy)
    #
    # Cached Engine(power=150, fuel=Fuel.Petrol)
    # Cached Wheel(diameter=19, material=Material.Alloy)
    # Car:
    # 	type = CarType.SUV
    # 	color = CarColor.Red
    # 	engine = Engine(power=150, fuel=Fuel.Petrol)
    # 	wheel = Wheel(diameter=19, material=Material.Alloy)
    #
    # New Engine(power=110, fuel=Fuel.Electric)
    # New Wheel(diameter=20, material=Material.Alloy)
    # Car:
    # 	type = CarType.Sedan
    # 	color = CarColor.White
    # 	engine = Engine(power=110, fuel=Fuel.Electric)
    # 	wheel = Wheel(diameter=20, material=Material.Alloy)
    #
    # New Engine(power=140, fuel=Fuel.Diesel)
    # Cached Wheel(diameter=18, material=Material.Alloy)
    # Car:
    # 	type = CarType.SUV
    # 	color = CarColor.Grey
    # 	engine = Engine(power=140, fuel=Fuel.Diesel)
    # 	wheel = Wheel(diameter=18, material=Material.Alloy)
    #
    # New Engine(power=150, fuel=Fuel.Electric)
    # Cached Wheel(diameter=20, material=Material.Alloy)
    # Car:
    # 	type = CarType.Sedan
    # 	color = CarColor.Grey
    # 	engine = Engine(power=150, fuel=Fuel.Electric)
    # 	wheel = Wheel(diameter=20, material=Material.Alloy)
