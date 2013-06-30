'''
Created on Jun 29, 2013

@author: smclaughlin
'''

import threading
import time

import RPi.GPIO as pi

import random

class ButtonThread(threading.Thread):
        def __init__(self,queue,moods):
            super(ButtonThread,self).__init__()
            self.running=True
            self.queue = queue
            
            # initialize GPIO pins and interrupts
            self.button = 7
            print "Setting up GPIO..."
            pi.setmode(pi.BOARD)
            pi.setup(self.button,pi.IN,pull_up_down=pi.PUD_DOWN)
            pi.add_event_detect(self.button,pi.BOTH,callback=self.changed, bouncetime=10)
            print "Done"
            self.startTime = None
            self.moods = moods
            
        def changed(self,arg):
            if(pi.input(self.button)):
                self.startTime = time.time()
            else:
                if(self.startTime):
                    index = random.randint(0,len(self.moods)-1)
                    self.queue.put((self.moods.keys()[index],True))
                    print 'Button Up!'
                self.startTime = None
        
        def run(self):
            while(self.running):
                if(self.startTime):
                    if(time.time()-self.startTime > 2):
                        print "Turn Off!"
                        self.queue.put(("<off>",True))
                        self.startTime = None
                time.sleep(0.01)
