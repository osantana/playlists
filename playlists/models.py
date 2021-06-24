class Track:
    def __init__(self, name, artist, album, playlists=None, service='applemusic'):
        self.name = name
        self.artist = artist
        self.album = album
        self.service = service

        if playlists is None:
            playlists = []
        self.playlists = playlists

    def set_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)

    def send(self, client):
        return client.add_track(self)


class Playlist:
    def __init__(self, name, description, tracks=None):
        self.name = name
        self.description = description
        self.tracks = []

        if tracks is None:
            return

        for track in tracks:
            self.add_track(track)

    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, item):
        return self.tracks[item]

    def add_track(self, track):
        track.set_playlist(self)
        self.tracks.append(track)
