from pygame import *
from audioController import * 

print "test"

list = AudioController()
list.selectPlaylist("red")
list.songSelect()

while mixer.music.get_busy():
    pass