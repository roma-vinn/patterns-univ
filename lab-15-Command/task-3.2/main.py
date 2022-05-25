from controller import Controller
from lamp import Lamp


def main():
    kitchen_lamp = Lamp('Kitchen')
    hall_lamp = Lamp('Hall')
    bedroom_lamp = Lamp('Bedroom')
    bathroom_lamp = Lamp('Bathroom')

    controller_kitchen_lamp = Controller(target=kitchen_lamp)
    controller_hall_lamp = Controller(target=hall_lamp)
    controller_bedroom_lamp = Controller(target=bedroom_lamp)
    controller_bathroom_lamp = Controller(target=bathroom_lamp)

    controller_universal = Controller(target=[kitchen_lamp, hall_lamp, bedroom_lamp, bathroom_lamp])

    # Simulation
    controller_kitchen_lamp.on()
    controller_hall_lamp.on()
    controller_bedroom_lamp.on()

    controller_kitchen_lamp.off()
    controller_hall_lamp.off()
    controller_bedroom_lamp.off()

    controller_bedroom_lamp.on()
    controller_bathroom_lamp.on()

    controller_universal.off()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Kitchen: Light is on
    # Hall: Light is on
    # Bedroom: Light is on
    # Kitchen: Light is off
    # Hall: Light is off
    # Bedroom: Light is off
    # Bedroom: Light is on
    # Bathroom: Light is on
    # Bedroom: Light is off
    # Bathroom: Light is off
