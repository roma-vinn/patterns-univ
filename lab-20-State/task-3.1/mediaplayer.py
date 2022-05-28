from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from state import State
from state import StoppedState


class MediaPlayer:
    def __init__(self):
        self._state: State = StoppedState()
        self._tracks: list[str] = []
        self._cur_track_num = 0

    def get_cur_track(self) -> str:
        return self._tracks[self._cur_track_num]

    def set_cur_track_num(self, track_num: int):
        if 0 <= track_num < len(self._tracks):
            self._cur_track_num = track_num
        else:
            print(f'Track num should be in range [0, {len(self._tracks)}]')

    def get_cur_track_num(self) -> int:
        return self._cur_track_num

    def get_tracks(self) -> list[str]:
        return self._tracks

    def add_track(self, track: str):
        self._tracks.append(track)

    def set_state(self, state: State):
        self._state = state

    def get_state(self) -> State:
        return self._state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def stop(self):
        self._state.stop(self)

    def next(self):
        self._state.next(self)

    def prev(self):
        self._state.prev(self)
