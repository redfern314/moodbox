'''
Created on Jun 29, 2013

@author: smclaughlin
'''

import threading
import time
import pygame

from ..BulbColorLib import BulbColorLib
from ..audioController import AudioController as AC

ipAddress = "192.168.1.148"

class MoodThread(threading.Thread):
        def __init__(self,queue,moods):
            super(MoodThread,self).__init__()
            self.running=True
            self.queue = queue
            ipFormat = "http://%s/api/newdeveloper/lights/%d/state"
            allFormat = "http://%s/api/newdeveloper/groups/0/action" % ipAddress
            self.bulbAddresses = [ipFormat % (ipAddress,i) for i in xrange(1,4)]
            self.bulbAddresses = [allFormat] + self.bulbAddresses
            
            self.audio = AC()

            self.bulbLib1 = BulbColorLib(self.bulbAddresses[1],moods)
            self.bulbLib2 = BulbColorLib(self.bulbAddresses[2],moods)
            self.bulbLib3 = BulbColorLib(self.bulbAddresses[3],moods)
	    
	    self.bulbLib1.bulbOff()
	    self.bulbLib2.bulbOff()
	    self.bulbLib3.bulbOff()

	    self.off = True
            
        def run(self):
            while(self.running):
                if(not self.queue.empty()):
                    mood,fromButton = self.queue.get()
	            print mood
                    if(mood == "<off>"):
                        self.audio.stop()
                        self.bulbLib1.bulbOff()
                        self.bulbLib2.bulbOff()
                        self.bulbLib3.bulbOff()
			self.audio.color = ""
			self.off = True
                    else:
			if(fromButton and self.off):
 			    #starup
			    self.audio.selectPlaylist("WHITE")
			    self.audio.selectNextSong() 
			    self.bulbLib1.colorLoopOn()
			    self.bulbLib2.colorLoopOn()
			    self.bulbLib3.colorLoopOn()
			else:
                            self.audio.selectPlaylist(mood)
                            self.audio.selectNextSong()
                            self.bulbLib1.setMood(mood)
                            self.bulbLib2.setMood(mood)
                            self.bulbLib3.setMood(mood)
		        self.off = False
                elif (not pygame.mixer.music.get_busy() and (not self.audio.color=="")):
                    self.audio.selectNextSong()
                time.sleep(0.01)
                
if __name__ == '__main__':
        mt = MoodThread(None) 
