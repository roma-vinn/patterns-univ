from abc import ABC, abstractmethod
from lamp import Lamp


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandOn(Command):
    def __init__(self, target: Lamp):
        self._target = target

    def execute(self):
        self._target.light_on()


class CommandOff(Command):
    def __init__(self, target: Lamp):
        self._target = target

    def execute(self):
        self._target.light_off()
