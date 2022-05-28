from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from state import State
from state import OffState


class Fan:
    def __init__(self):
        self._state = OffState()

    def set_state(self, state: State):
        self._state = state

    def get_state(self) -> State:
        return self._state

    def turn_up(self):
        self._state.turn_up(self)

    def turn_down(self):
        self._state.turn_down(self)
