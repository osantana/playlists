class Track:
    def __init__(self, name, artist, album):
        self.name = name
        self.artist = artist
        self.album = album


class Playlist:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tracks = []

    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, item):
        return self.tracks[item]

    def add_track(self, track):
        self.tracks.append(track)
