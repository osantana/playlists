import pytest

from playlists.models import Playlist, Track


def test_basic_track():
    track = Track('Song', 'Author', 'Album')
    assert track.name == 'Song'
    assert track.artist == 'Author'
    assert track.album == 'Album'
    assert track.playlists == []


def test_empty_playlist():
    playlist = Playlist('Name', 'Description')
    assert playlist.name == 'Name'
    assert playlist.description == 'Description'
    assert len(playlist) == 0
    with pytest.raises(IndexError):
        assert playlist[0] == 'index-error'


def test_filled_playlist():
    track = Track('Song', 'Author', 'Album')
    playlist = Playlist('Name', 'Description', tracks=[track])

    assert track in playlist.tracks
    assert playlist in track.playlists


def test_add_track_to_playlist():
    track = Track('Song', 'Author', 'Album')
    playlist = Playlist('Name', 'Description')

    playlist.add_track(track)

    assert track in playlist.tracks
    assert playlist in track.playlists
