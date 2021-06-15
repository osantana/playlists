import json

import pytest

from playlists.exceptions import InvalidPlaylistFile
from playlists.storages import PropertyListStorage, JSONStorage


def test_basic_plist_storage(plist_xml_filename):
    storage = PropertyListStorage(plist_xml_filename)
    playlists = storage.get_playlists()
    assert len(playlists) == 1

    playlist = playlists[0]
    assert playlist.name == 'Sample Playlist'
    assert playlist.description == 'Description of the Sample Playlist'
    assert len(playlist) == 5


def test_plist_track_ordering(plist_xml_filename):
    storage = PropertyListStorage(plist_xml_filename)
    playlist = storage.get_playlists()[0]

    assert playlist[0].name == 'Megablast (Hip Hop On Precinct 13) [7" Mix]'
    assert playlist[1].name == 'Beat Dis (7" US Mix)'
    assert playlist[2].name == 'Harry Houdini'
    assert playlist[3].name == 'You Spind Me Round'
    assert playlist[4].name == 'Smalltown Boy'


def test_fail_invalid_plist_storage(plist_invalid_xml_filename):
    storage = PropertyListStorage(plist_invalid_xml_filename)
    with pytest.raises(InvalidPlaylistFile):
        storage.get_playlists()


def test_basic_json_storage_serialization(playlists, empty_json_filename):
    storage = JSONStorage(empty_json_filename)
    serialized = storage.serialize(playlists)

    data = json.loads(serialized)
    assert len(data) == 1

    playlist_data = data[0]
    assert playlist_data['name'] == 'Sample Playlist'
    assert len(playlist_data['tracks']) == 5

    tracks = playlist_data['tracks']
    assert tracks[0]['track'] == 'Megablast (Hip Hop On Precinct 13) [7" Mix]'
    assert tracks[1]['track'] == 'Beat Dis (7" US Mix)'
    assert tracks[2]['track'] == 'Harry Houdini'
    assert tracks[3]['track'] == 'You Spind Me Round'
    assert tracks[4]['track'] == 'Smalltown Boy'


def test_basic_json_storage_save(playlists, empty_json_filename):
    storage = JSONStorage(empty_json_filename)
    storage.save(playlists)

    with open(empty_json_filename, 'r') as jsonfile:
        data = jsonfile.read()

    assert storage.serialize(playlists) == data
