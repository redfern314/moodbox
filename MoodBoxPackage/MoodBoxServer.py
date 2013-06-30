'''
Created on Jun 29, 2013

@author: smclaughlin
'''
import re
import json
import BaseHTTPServer

from MoodBoxThreads import ButtonThread,MoodThread
from Queue import Queue

postMatch = re.compile("\s*(\w+)\s*:\s*(\w+)\s*")

class MoodBoxHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == "/"):
            self.send_response(200)
            self.end_headers()
            messageQueue.put("Recieved!!")
            self.wfile.write("<b>Hello!</b>")
        else:
            self.send_error(404)
            
    def do_POST(self):
        import time
        start = time.time()
        contentLen = int(self.headers.getheader('content-length'))
        requestString = self.rfile.read(contentLen)
        m = postMatch.match(requestString)
        if(m):
            key,value = m.groups()
            if(key.lower() == "setmood"):
                print "Putting Value:",value
                messageQueue.put(value)
                self.send_response(200)
                self.end_headers()
                self.wfile.write("success!")
                print"Time:", time.time()-start
                return
        
        self.send_error(400)

messageQueue = Queue()

def Run(path):
    with open(path) as f:
        moods = json.load(f)
    
    httpd = BaseHTTPServer.HTTPServer(('0.0.0.0',8080),MoodBoxHandler)
    
    threads = {
        "Button Thread": ButtonThread.ButtonThread,
        "Mood Thread": MoodThread.MoodThread
    }
    
    for k in threads:
        threads[k] = threads[k](messageQueue,moods)
        
    for k in threads:
        threads[k].start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Exiting..."
   
    for k,v in threads.items():
        print "Joining",k+"..."
        v.running = False
        v.join()

    httpd.server_close()