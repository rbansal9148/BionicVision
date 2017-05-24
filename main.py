import boot
import helper
from time import sleep
import tempfile
import picamera

boot.detect_camera()
boot.internet_on() #If no connection to MCS is established than it will exit
print "Waiting 2 secs"
#sleep(2)
boot.isMCSWorking()


_url = 'https://southeastasia.api.cognitive.microsoft.com/vision/v1.0/analyze'
_key = 'd1008b4f501046f1b3dc2994e3bc50c7'
_maxNumRetries = 10
params = {'visualFeatures' : 'Color, Categories, Description'} 
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'
jsonObj = None

with tempfile.NamedTemporaryFile(mode="rb") as jpg:
	camera = picamera.PiCamera()
	print "Created camera instance"
	camera.resolution = (1920, 1080)
	camera.capture(jpg)
	data = jpg.read()
time.sleep(2.0)
result = helper.processRequest(json, _url, data, headers, params)
if result is not None:
	description = helper.renderResult(result)
	print description
