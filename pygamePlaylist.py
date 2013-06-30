from pygame import *
import os

mixer.init()
os.environ["SDL_VIDEODRIVER"]="dummy"
display.init()
display.set_mode((1,1))

mixer.music.load("1s.mp3")
mixer.music.set_endevent(USEREVENT)
mixer.music.play()

print(event.wait())
