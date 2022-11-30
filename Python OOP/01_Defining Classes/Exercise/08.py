from project.song import Song
from project.band import Band
from project.album import Album

# song = Song("songname", 3, False)
# # song2 = Song("songname2", 3, False)
# album = Album("albumname", song, song)
# band = Band("bandname")
# print(band.add_album(album))
# album.publish()
# print(band.remove_album("albumname"))

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
