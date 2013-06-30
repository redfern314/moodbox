import time
import random
import os, sys
import pyaudio
import mad

import pygame
import ossaudiodev
import wave

class Playlist:
    'Class for playlist handling'
    color = ""

    def selectPlaylist(self, playlist_color):
        Playlist.color = playlist_color  
    
    # this function should be called when:
     # new playlist is selected
     # song ends
    def songSelect(self):
        path = "playlists/" + Playlist.color 
        song_selection = random.randint(1,3)
        #song_selection = "1s"
        full_file_name = path + "/" + str(song_selection) + ".mp3"
        #full_file_name = path + "/" + song_selection + ".mp3"
        self.play(full_file_name)

    
    def callback(self, in_data, frame_count, time_info, status):
        data = self.mf.read(48000)
        return (data, pyaudio.paContinue)
        #data = self.mf.read(frame_count)
        #return (data, pyaudio.paContinue)


    def play(self, filename):
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
        p.terminate()
    









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
