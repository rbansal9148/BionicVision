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

print 'Importing urllib2'
install_package('urllib2')
import urllib2
print 'Imported Successfully'

def internet_on():
	try:
		urllib2.urlopen('http://216.58.192.142', timeout = 1)
		print 'Server is reachable and available'
		return True
	except	urllib2.URLError as err:
		sys.exit()

print 'Checking for AWS Availability...'
internet_on()

