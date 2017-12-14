import RPi.GPIO as GPIO
import time
import scene_descriptor
import picamera

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Instatiate camera
camera = picamera.PiCamera()

try:
	# True for  getting button responses
	while True:
    	button_state = GPIO.input(23)
		
    	if button_state == False:
        	print('Capture And Detect...')
       		time.sleep(0.2)
       		key=scene_descriptor.getKey()
        	key = '431346910fd7435180c72f27b72c5f8d'
        	try:
            	scene_descriptor.bootstrap(key)
               scene_descriptor.camera_PR(key, camera)
             except:
               print "Some Unknown Error"

except:
    GPIO.cleanup()
