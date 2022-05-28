from mediaplayer import MediaPlayer


def main():
    media_player = MediaPlayer()
    media_player.add_track(track='track1')
    media_player.add_track(track='track2')
    media_player.add_track(track='track3')
    media_player.add_track(track='track4')
    media_player.add_track(track='track5')
    media_player.add_track(track='track6')

    media_player.play()
    media_player.pause()
    media_player.play()
    media_player.next()
    media_player.next()
    media_player.prev()
    media_player.stop()
    media_player.play()
    media_player.stop()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Play: track1
    # Pause: track1
    # Resume: track1
    # Play next: track2
    # Play next: track3
    # Play previous: track2
    # Stop: track2
    # Play: track2
    # Stop: track2
