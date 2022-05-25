from abc import ABC, abstractmethod
from typing import Union
from device import Device
from command import CommandOn, CommandOff, CommandVolumeUp, CommandVolumeDown, CommandNextChannel, CommandPrevChannel


class _Controller(ABC):
    @abstractmethod
    def device_on(self):
        pass

    @abstractmethod
    def device_off(self):
        pass

    @abstractmethod
    def device_volume_up(self):
        pass

    @abstractmethod
    def device_volume_down(self):
        pass

    @abstractmethod
    def device_next_channel(self):
        pass

    @abstractmethod
    def device_prev_channel(self):
        pass


class Controller(_Controller):
    def __init__(self, target: Union[Device, list[Device]]):
        self._commands_on = []
        self._commands_off = []
        self._commands_volume_up = []
        self._commands_volume_down = []
        self._commands_next_ch = []
        self._commands_prev_ch = []
        if isinstance(target, Device):
            self._commands_on.append(CommandOn(target))
            self._commands_off.append(CommandOff(target))
            self._commands_volume_up.append(CommandVolumeUp(target))
            self._commands_volume_down.append(CommandVolumeDown(target))
            self._commands_next_ch.append(CommandNextChannel(target))
            self._commands_prev_ch.append(CommandPrevChannel(target))
        elif isinstance(target, list):
            for t in target:
                if isinstance(t, Device):
                    self._commands_on.append(CommandOn(t))
                    self._commands_off.append(CommandOff(t))
                    self._commands_volume_up.append(CommandVolumeUp(t))
                    self._commands_volume_down.append(CommandVolumeDown(t))
                    self._commands_next_ch.append(CommandNextChannel(t))
                    self._commands_prev_ch.append(CommandPrevChannel(t))
                else:
                    raise ValueError(f'Target should be of class <Device>, got: {type(t)}')

    def device_on(self):
        for command in self._commands_on:
            command.execute()

    def device_off(self):
        for command in self._commands_off:
            command.execute()

    def device_volume_up(self):
        for command in self._commands_volume_up:
            command.execute()

    def device_volume_down(self):
        for command in self._commands_volume_down:
            command.execute()

    def device_next_channel(self):
        for command in self._commands_next_ch:
            command.execute()

    def device_prev_channel(self):
        for command in self._commands_prev_ch:
            command.execute()
