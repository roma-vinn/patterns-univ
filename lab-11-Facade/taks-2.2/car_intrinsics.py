class Accelerator:
    @staticmethod
    def press():
        print('Pressing accelerator down')

    @staticmethod
    def lift():
        print('Lifting accelerator up')


class Clutch:
    @staticmethod
    def press():
        print('Pressing clutch down')

    @staticmethod
    def lift():
        print('Lifting clutch up')


class GearStick:
    def __init__(self):
        self._gear = 0

    def change_gear(self, gear: int):
        assert 0 <= gear <= 5, 'gear must be in range [0, 5]'
        self._gear = gear
        print(f'Changing gear to {gear}')


class Handbrake:
    def __init__(self):
        self._is_up = False

    def push_down(self):
        self._is_up = False
        print('Pushing down handbrake')

    def lift_up(self):
        self._is_up = False
        print('Lifting up handbrake')


class Ignition:
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print('Turning ignition on')

    def turn_off(self):
        self._is_on = False
        print('Turning ignition off')
