import pytest

from playlists.models import Playlist, Track


def test_basic_playlist():
    playlist = Playlist('Name', 'Description')
    assert playlist.name == 'Name'
    assert playlist.description == 'Description'
    assert len(playlist) == 0
    with pytest.raises(IndexError):
        assert playlist[0] == 'index-error'


def test_basic_track():
    track = Track('Song', 'Author', 'Album')
    assert track.name == 'Song'
    assert track.artist == 'Author'
    assert track.album == 'Album'
