from typing import List
from project.song import Song


class Album:
    name: str
    songs: List[Song]
    published: bool

    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = []
        self.published = False
        for song in songs:
            self.add_song(song)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        songs_to_be_removed = [s for s in self.songs if s.name == song_name]
        if not songs_to_be_removed:
            return "Song is not in the album."

        self.songs.remove(songs_to_be_removed[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        album_lines = [f"Album {self.name}"]
        songs_lines = [f"== {s.get_info()}" for s in self.songs]
        return "\n".join(album_lines + songs_lines) + "\n"
