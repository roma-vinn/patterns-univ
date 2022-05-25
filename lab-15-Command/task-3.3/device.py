from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def next_channel(self):
        pass

    @abstractmethod
    def prev_channel(self):
        pass


class TV(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 50
        self._channel = 1

    def on(self):
        if self._is_on:
            return
        print('TV is on.')
        self._is_on = True

    def off(self):
        if not self._is_on:
            return
        print('TV is off.')
        self._is_on = False

    def volume_up(self):
        if not self._is_on:
            return
        self._volume += 1
        print(f'TV volume = {self._volume}')

    def volume_down(self):
        if not self._is_on:
            return
        self._volume -= 1
        print(f'TV volume = {self._volume}')

    def next_channel(self):
        if not self._is_on:
            return
        self._channel += 1
        print(f'TV channel = {self._channel}')

    def prev_channel(self):
        if not self._is_on:
            return
        self._channel -= 1
        print(f'TV channel = {self._channel}')


class Radio(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 50
        self._channel = 1

    def on(self):
        if self._is_on:
            return
        print('Radio is on.')
        self._is_on = True

    def off(self):
        if not self._is_on:
            return
        print('Radio is off.')
        self._is_on = False

    def volume_up(self):
        if not self._is_on:
            return
        self._volume += 1
        print(f'Radio volume = {self._volume}')

    def volume_down(self):
        if not self._is_on:
            return
        self._volume -= 1
        print(f'Radio volume = {self._volume}')

    def next_channel(self):
        if not self._is_on:
            return
        self._channel += 1
        print(f'Radio channel = {self._channel}')

    def prev_channel(self):
        if not self._is_on:
            return
        self._channel -= 1
        print(f'Radio channel = {self._channel}')
