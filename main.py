import RPi.GPIO as GPIO
import time
import scene_descriptor
import picamera
import boot
import OCR

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Instatiate camera
camera = picamera.PiCamera()
boot.detect_camera()

_key_DeepAI = 'aedb7e46-3664-494b-b30d-dfa5dff0429d'
key = '431346910fd7435180c72f27b72c5f8d'
helper.bootstrap_MSC(key)


try:
	# True for  getting button responses
	while True:
    	button_state1 = GPIO.input(23)
    	button_state2 = GPIO.input(23)
    	button_state3 = GPIO.input(23)

    	if button_state1 == False:
        	print('Capture And Detect...')
			# key = scene_descriptor.getKey()
        	try:
        		scene_descriptor.camera_PR(key, camera)
				scene_descriptor.camera_PR_DeepAI(_key_DeepAI, camera)
    		except:
        		print "Some Unknown Error"

		if button_state2 == False:
			print('OCR Activated...')
			# time.sleep(0.2)
			imageName = r'./abc.jpg'
			camera.capture(imageName)
			print OCR.get_string('./' + imageName)

		if button_state3 == False:
			print('Sending Emergency Message...')
			time.sleep(0.2)

except:
    GPIO.cleanup()
