import boot
import helper
from time import sleep
# import picamera
from io import BytesIO
import json


# Get these from MSC Cognitive Serivices
_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'
# Store key in 'key' filename
_key = ''

try:
	file = open(r'./key', 'r')
	_key = file.read()
	_key = _key[:-1]
	# print _key
except:
	print "Key not found. Exiting..."
else:
	file.close()

# boot.detect_camera()
boot.internet_on()  # If no connection to MCS is established than it will exit
boot.isMCSWorking(_url, _key)

# API parameters
#_url = 'https://southeastasia.api.cognitive.microsoft.com/vision/v1.0/analyze'
#_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/'
#_url = 'https://
_maxNumRetries = 10
params = {'visualFeatures': 'Color, Categories, Description'}
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'
jsonObj = None

# camera = picamera.PiCamera()
imageName = r'./abc.jpg'
# camera.capture(imageName)
with open(imageName, 'rb') as f:
	data = f.read()

# sleep(2.0)
print "Sending Request"
result = helper.processRequest(json, _url, data, headers, params)
if result is not None:
	description = helper.renderResult(result)
	print 'Output: "' + description + '"'
	helper.output_audio(description)
