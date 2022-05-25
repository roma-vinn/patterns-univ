from abc import ABC, abstractmethod
from device import Device


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandOn(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.on()


class CommandOff(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.off()


class CommandVolumeUp(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.volume_up()


class CommandVolumeDown(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.volume_down()


class CommandNextChannel(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.next_channel()


class CommandPrevChannel(Command):
    def __init__(self, target: Device):
        self._target = target

    def execute(self):
        self._target.prev_channel()
