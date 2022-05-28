from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fan import Fan
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def turn_up(self, fan: Fan):
        pass

    @abstractmethod
    def turn_down(self, fan: Fan):
        pass


class OffState(State):
    def turn_up(self, fan: Fan):
        fan.set_state(LowState())
        print('Turning on: Low')

    def turn_down(self, fan: Fan):
        pass


class LowState(State):
    def turn_up(self, fan: Fan):
        fan.set_state(MediumState())
        print('Increasing speed: Medium')

    def turn_down(self, fan: Fan):
        fan.set_state(OffState())
        print('Turning fan off')


class MediumState(State):
    def turn_up(self, fan: Fan):
        fan.set_state(HighState())
        print('Increasing speed: High')

    def turn_down(self, fan: Fan):
        fan.set_state(LowState())
        print('Decreasing speed: Low')


class HighState(State):
    def turn_up(self, fan: Fan):
        pass

    def turn_down(self, fan: Fan):
        fan.set_state(MediumState())
        print('Decreasing fan: Medium')
