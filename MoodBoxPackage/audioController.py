import time
import random
import os, sys

import wave
from pygame import *

class AudioController:
    'Class for playlist handling'

    def selectPlaylist(self, playlist_color):
        self.color = playlist_color  

    def __init__(self):
        mixer.init()
	self.color = ""
        os.environ["SDL_VIDEODRIVER"]="dummy"
        display.init()
        display.set_mode((1,1))

    
    # this function should be called when:
     # new playlist is selected
     # song ends
    def selectNextSong(self):
        path = "/home/pi/playlists/" + self.color 
        song_selection = random.randint(1,3)
        files = os.listdir(path)

	index = random.randint(0,len(files) - 1 )
        full_file_name = path + "/" + files[index] 
        self.play(full_file_name)

    
    def callback(self, in_data, frame_count, time_info, status):
        data = self.mf.read(48000)
        return (data, pyaudio.paContinue)
        #data = self.mf.read(frame_count)
        #return (data, pyaudio.paContinue)

    def stop(self):
        mixer.music.fadeout(500)

    def play(self, filename):
	print "PLAYING MUSIC"
        if mixer.music.get_busy():
            self.stop()
        mixer.music.load(filename)
        mixer.music.play()



# def run(queue,moods):
#     if not queue.empty():
#         newmood = queue.get()
#         playlist.selectPlaylist(newmood)
#         playlist.selectSong()
#     elif not mixer.music.get_busy():
#         playlist.selectSong()







#######################BELOW NOT USED##################
"""

    #Play a sound file
    def play_complex(self,filename):
                
        print "opening file"
        sound_file = None
        sound = None

        try:
            print "opening file"
            sound_file = wave.open(filename,'rb')

            print "getting parameters"
            (nc, sw, fr, nf, comptype, compname) = sound_file.getparams()

            print "parameters were",  (nc, sw, fr, nf, comptype, compname)
            print "opening audio"
            sound = ossaudiodev.open('w')

            print "setting parameters"
            sound.setparameters(ossaudiodev.AFMT_S16_NE, nc, fr)

            print "readframes"
            data = sound_file.readframes(65536)
            while data:
                sound.write(data, None, True)
                data = sound_file.readframes(65536)

                sound.flush()
                sound.sync()

        except IOError, e:
            print str(e)

        finally:
            if sound != None and sound_file != None: 
                print "closing file"
                sound_file.close()

                print "closing sound device"
                sound.close()

    if __name__ == '__main__':
        if len(sys.argv) is 2:
            play(sys.argv[1])
        else:
            print 'Usage: %s filename' % sys.argv[0]




    def printCurrent(self):
        print Playlist.color


    def play_game(self,filename):
        print "playing file"
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()


#EXAMPLE CODE ->>>
        #files = os.listdir(path)
        #for filename in files:
        #    print filename
    def notWORKINGplay(self, filename):
        self.mf = mad.MadFile(filename)
        p = pyaudio.PyAudio()
        stream = p.open(format =
                    p.get_format_from_width(pyaudio.paInt32),
                    channels = 2,
                    #rate = self.mf.samplerate(),
                    rate = 48000,
                    output = True,
                    stream_callback = self.callback)
                    
        
        print self.mf.samplerate()
        data = self.mf.read()
## OLD (WORKING) ##
#        while data != None:
#            stream.write(data)
#            data = self.mf.read()
## OLD END##

##NEW
        stream.start_stream()

        while stream.is_active():
            time.sleep(0.0001)

        stream.stop_stream()
## END NEW##



#        stream.close()
        p.terminate()"""
    



