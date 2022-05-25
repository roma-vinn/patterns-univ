from typing import Union
from lamp import Lamp
from command import CommandOn, CommandOff


class Controller:
    def __init__(self, target: Union[Lamp, list[Lamp]]):
        self._commands_on = []
        self._commands_off = []
        if isinstance(target, Lamp):
            self._commands_on.append(CommandOn(target))
            self._commands_off.append(CommandOff(target))
        elif isinstance(target, list):
            for t in target:
                if isinstance(t, Lamp):
                    self._commands_on.append(CommandOn(t))
                    self._commands_off.append(CommandOff(t))
                else:
                    raise ValueError(f'Target should be of class <Lamp>, got: {type(t)}')

    def on(self):
        for command in self._commands_on:
            command.execute()

    def off(self):
        for command in self._commands_off:
            command.execute()
