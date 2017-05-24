import boot
import helper
from time import sleep
from io import BytesIO
from picamera import PiCamera

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

data = BytesIO()
camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture(data, 'jpeg')

time.sleep(2.0)
result = helper.processRequest(json, _url, data, headers, params)
if result is not None:
	description = helper.renderResult(result)
	print description
