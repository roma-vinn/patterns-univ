from car_intrinsics import Ignition, GearStick, Accelerator, Handbrake, Clutch


class Car:
    """Facade for interaction with car intrinsics"""
    def __init__(self):
        self._ignition = Ignition()
        self._clutch = Clutch()
        self._accelerator = Accelerator()
        self._gear_stick = GearStick()
        self._handbrake = Handbrake()

    def drive(self):
        self._ignition.turn_on()
        self._clutch.press()
        self._gear_stick.change_gear(1)
        self._accelerator.press()
        self._clutch.lift()
        self._handbrake.push_down()
        self._accelerator.press()
        self._clutch.press()
