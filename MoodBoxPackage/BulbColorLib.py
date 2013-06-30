import requests

# converting between raw HSV value to one usable by bulb:
# bulbHue = H*182.04
# bulbSat = Sat/100*255

OFF = '{"on":false}'
ON = '{"on":true}'		 

# moods dictionary
# (key, value)
# (mood_string, (H,S))
moods = { 
'TAN': (42, 38),
'CYAN':(182,100),
'GREEN':(167,100),
'PINK':(315,93),
'PURPLE':(284,100)
}

# 42 , 38 , 100  # yellow/tan
# 182 , 100 , 100 # cyan
# 167, 100 # green
# 315 , 93 , 100 # pink
# 284, 100 , 100  # purple
 
class BulbColorLib:
	bulbState = ''
	moodsDictionary = {}

	def __init__(self, address, moodsDict={}):
		self.bulbState = address 
		self.moodsDictionary = moodsDict

	def bulbOn(self):
		resp = requests.put(self.bulbState,ON)
		print resp.content

	def bulbOff(self):
		resp = requests.put(self.bulbState,OFF)
		print resp.content

	def colorLoopOn(self):
		resp = requests.put(self.bulbState, '{"on":true, "effect":"colorloop"}')
		print resp.content

	def colorLoopOff(self):
		resp = requests.put(self.bulbState, '{"on":true, "effect":"none"}')
		print resp.content

	def convertRawHueToBulb(self, H):
		return int(H*182.04)

	def convertRawSatToBulb(self, S):
		return int((S)/100.0*255)

	# will turn on the bulb and set the appropriate Hue
	def bulbHue(self, H):
		return '{"on":true, "hue":' + str(self.convertRawHueToBulb(H)) + '}'

	def bulbSat(self, S):
	 	return '  {"sat":' + str(self.convertRawSatToBulb(S)) + '}'

	def setColor(self, H, S) :
		self.colorLoopOff()
		resp = requests.put(self.bulbState, self.bulbHue(H))
		print resp.content
		resp = requests.put(self.bulbState, self.bulbSat(S))
		print resp.content

	def setMood(self, mood):
		self.colorLoopOff()
		print "Setting Mood"
		if(mood in self.moodsDictionary):
			moodHsv = self.moodsDictionary[mood]
			self.setColor(moodHsv[0], moodHsv[1])
		else:
			self.setColor(0,0)

if __name__ == "__main__":
	print "Welcome to Moodbox"

	bulb3Address = 'http://192.168.1.148/api/newdeveloper/lights/3'
	bulb1Address = 'http://192.168.1.148/api/newdeveloper/lights/1'

	bulb = BulbColorLib(bulb3Address, moods)
	bulb.setMood('PURPLE')
