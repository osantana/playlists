import json
import plistlib

from .exceptions import InvalidPlaylistFile
from .models import Playlist, Track


class Storage:
    def __init__(self, filename):
        self.filename = filename


class PropertyListStorage(Storage):
    def load(self):
        with open(self.filename, 'rb') as file_storage:
            plist = plistlib.load(file_storage)

        if 'Tracks' not in plist or 'Playlists' not in plist:
            raise InvalidPlaylistFile(f'{self.filename} does not contains tracks or playlists.')

        return plist

    # noinspection PyMethodMayBeStatic
    def _get_tracks(self, plist):
        tracks = {}
        for track_id, track_data in plist['Tracks'].items():
            track = Track(
                name=track_data['Name'],
                artist=track_data['Artist'],
                album=track_data['Album'],
            )
            tracks[track_id] = track
        return tracks

    def get_playlists(self):
        plist = self.load()
        tracks = self._get_tracks(plist)

        playlists = []
        for playlist_data in plist['Playlists']:
            playlist = Playlist(
                name=playlist_data['Name'],
                description=playlist_data['Description'],
            )
            for track_data in playlist_data['Playlist Items']:
                track_id = str(track_data['Track ID'])
                playlist.add_track(tracks[track_id])
            playlists.append(playlist)

        return playlists


class JSONStorage(Storage):
    # noinspection PyMethodMayBeStatic
    def _to_data(self, playlists):
        playlists_data = []
        for playlist in playlists:
            tracks_data = []
            for track in playlist.tracks:
                tracks_data.append({
                    'album': track.album,
                    'track': track.name,
                    'artist': track.artist,
                })

            playlists_data.append({
                'name': playlist.name,
                'tracks': tracks_data,
            })

        return playlists_data

    # noinspection PyMethodMayBeStatic
    def serialize(self, playlists):
        return json.dumps(self._to_data(playlists))

    def save(self, playlists):
        with open(self.filename, 'wb') as jsonfile:
            jsonfile.write(self.serialize(playlists).encode('ascii'))
