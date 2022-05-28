from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mediaplayer import MediaPlayer


class State(ABC):
    @abstractmethod
    def play(self, media_player: MediaPlayer):
        pass

    @abstractmethod
    def pause(self, media_player: MediaPlayer):
        pass

    @abstractmethod
    def stop(self, media_player: MediaPlayer):
        pass

    @staticmethod
    def next(media_player: MediaPlayer):
        cur_track_num = media_player.get_cur_track_num()
        if cur_track_num < len(media_player.get_tracks()) - 1:
            media_player.set_state(PlayingState())
            media_player.set_cur_track_num(cur_track_num + 1)
            print(f'Play next: {media_player.get_cur_track()}')
        else:
            print('Reached final track')

    @staticmethod
    def prev(media_player: MediaPlayer):
        cur_track_num = media_player.get_cur_track_num()
        if cur_track_num > 0:
            media_player.set_state(PlayingState())
            media_player.set_cur_track_num(cur_track_num - 1)
            print(f'Play previous: {media_player.get_cur_track()}')
        else:
            print('Reached first track')


class PauseState(State):
    def play(self, media_player: MediaPlayer):
        media_player.set_state(PlayingState())
        print(f'Resume: {media_player.get_cur_track()}')

    def pause(self, media_player: MediaPlayer):
        pass

    def stop(self, media_player: MediaPlayer):
        media_player.set_state(StoppedState())
        print(f'Stop: {media_player.get_cur_track()}')


class PlayingState(State):
    def play(self, media_player: MediaPlayer):
        pass

    def pause(self, media_player: MediaPlayer):
        media_player.set_state(PauseState())
        print(f'Pause: {media_player.get_cur_track()}')

    def stop(self, media_player: MediaPlayer):
        media_player.set_state(StoppedState())
        print(f'Stop: {media_player.get_cur_track()}')


class StoppedState(State):
    def play(self, media_player: MediaPlayer):
        media_player.set_state(PlayingState())
        print(f'Play: {media_player.get_cur_track()}')

    def pause(self, media_player: MediaPlayer):
        pass

    def stop(self, media_player: MediaPlayer):
        pass
