import sys
import helper
import time
import json
print 'Booting Up...'

def install_package(package):
	import importlib
	try:
		print 'Checking ' + package
		importlib.import_module(package)
	except ImportError:
		print package + ' not found'
		print 'Installing' + package
		import pip
		pip.main(['install', package])

def internet_on():
	try:
		import urllib2
		#To Do change the url to AWS server
		urllib2.urlopen('http://google.com', timeout = 3)
		print 'Internet is reachable and available'
		return True
	except	urllib2.URLError as err:
		print 'Not able to connect to Internet'
		sys.exit()

def detect_camera():
	import subprocess
	camdet = subprocess.check_output(["vcgencmd","get_camera"])
	int(camdet.strip()[-1]) #-- Removes the final CR character and gets only the "0" or "1" from detected status
	if (camdet):
		print "Camera detected"
	else:
		print "not detected"
		sys.exit()
		
def isMCSWorking():
	_url = 'https://southeastasia.api.cognitive.microsoft.com/vision/v1.0/analyze'
	_key = 'd1008b4f501046f1b3dc2994e3bc50c7'
	_maxNumRetries = 10
	params = {'visualFeatures' : 'Color, Categories, Description'} 
	headers = dict()
	headers['Ocp-Apim-Subscription-Key'] = _key
	headers['Content-Type'] = 'application/octet-stream'
	jsonObj = None
	imageName = r'./TestImages/a1.jpeg'
	time.sleep(2.0)
	with open(imageName, 'rb') as f:
		data = f.read()
	result = helper.processRequest(json, _url, data, headers, params)
	if result is not None:
		description = helper.renderResult(result)
		if 'woman' in description:
			print 'Test Case #1 : Passed'
			print 'MCS working correctly'
		else:
			print 'Test Case #1 : FAILED!!'
	else:
		print "Empty Result!!"
