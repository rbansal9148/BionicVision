import time
from datetime import datetime
import requests
import operator
import numpy as np
import json
import urllib2

def output_audio(aud):
	from boot import install_package
	from tempfile import TemporaryFile
	install_package('gtts')
	from gtts import gTTS
	tts = gTTS(text = aud, lang = 'en', slow = True)
	f = TemporaryFile()
	tts.write_to_fp(f)
	f.close()

def capture():
	from io import BytesIO
	from time import sleep
	from picamera import PiCamera

	# Create an in-memory stream
	my_stream = BytesIO()
	camera = PiCamera()
	camera.start_preview()
	# Camera warm-up time
	sleep(2)
	camera.capture(my_stream, 'jpeg')
	return my_stream
	
def processRequest( jsonObj, _url, data, headers, params):
    print('Uploading...')
    retries = 0
    result = None

    while True:
        response = requests.request( 'post', _url, json = jsonObj, data = data, headers = headers, params = params )
        if response.status_code == 429: 
            print( "Message: %s" % ( response.json()['message'] ) )
            if retries <= _maxNumRetries: 
                time.sleep(1)
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break
        elif response.status_code == 200 or response.status_code == 201:
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        elif response.status_code == 401:
        	print "Invalid Subscription Key"
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['message'] ) )
        break
    print('Complete!')
    time.sleep(1.0)
    return result

def renderResult (result) :
    descriptionText = result['description']['captions'][0]['text']
    return descriptionText
