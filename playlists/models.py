#!/usr/bin/env python3.9

class Playlist:
    def __len__(self):
        return 0


class Track:
    def __init__(self, title, author, album):
        self.title = title
        self.author = author
        self.album = album
