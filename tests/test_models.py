from playlists import Playlist, Track


def test_basic_playlist():
    playlist = Playlist()
    assert len(playlist) == 0


def test_basic_track():
    track = Track('Song', 'Author', 'Album')
    assert track.title == 'Song'
    assert track.author == 'Author'
    assert track.album == 'Album'
