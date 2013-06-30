from pygame import *
from audioController import * 

print "test"

playlist = AudioController()
playlist.selectPlaylist("red")
playlist.selectNextSong()

while mixer.music.get_busy():
    pass