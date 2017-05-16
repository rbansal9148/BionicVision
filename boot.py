import sys
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
		print 'Server is reachable and available'
		return True
	except	urllib2.URLError as err:
		print 'Not able to connect to AWS'
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
