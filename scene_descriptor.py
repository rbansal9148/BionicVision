import boot
import helper
from time import sleep
#import picamera
from io import BytesIO
import json
import sys


# Get these from MSC Cognitive Serivices
_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'
#_url = 'http://localhost:1337/api/detect'
# Store key in 'key' filename

def getkey():
	# Read key from file
	try:
		file = open(r'./key', 'r')
		_key = file.read()
		_key = _key[:-1]
		return _key
	except:
		print "Key not found. Exiting..."
		sys.exit()

def bootstrap(_key):
	boot.detect_camera()
	boot.internet_on()  # If no connection to MCS is established than it will exit
	boot.isMCSWorking(_url, _key)

# API parameters
#_url = 'https://southeastasia.api.cognitive.microsoft.com/vision/v1.0/analyze'
#_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/'



def camera_PR(_key, camera):
	_maxNumRetries = 10
	params = {'visualFeatures': 'Color, Categories, Description'}
	headers = dict()
	headers['Ocp-Apim-Subscription-Key'] = _key
	headers['Content-Type'] = 'application/octet-stream'
	jsonObj = None

	print 'start Test '

#	camera = picamera.PiCamera()
	imageName = r'./abc.jpg'
        print 'Middle Test'
	camera.capture(imageName)
	with open(imageName, 'rb') as f:
		data = f.read()
        print 'end Test'
	# sleep(2.0)
	print "Sending Request..."
	result = helper.processRequest(json, _url, data, headers, params)
	if result is not None:
		description = helper.renderResult(result)
		print 'Output: "' + description + '"'
		# helper.output_audio(description)
