from dataclasses import dataclass


@dataclass
class Song:
    title: str
    artist: str

class Chart:
    def __init__(self, path):
        pass

    @classmethod
    def discover(cls, path):
        pass
