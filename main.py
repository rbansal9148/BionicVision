import RPi.GPIO as GPIO
import time
import scene_descriptor
import picamera
import boot
import OCR

#import button1
#import button2
#import button3

#GPIO.setmode(GPIO.BCM)

#pin1 = 26
#pin2 = 23
#pin3 = 16

#GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Instatiate camera
camera = picamera.PiCamera()
boot.detect_camera()

_key_DeepAI = 'aedb7e46-3664-494b-b30d-dfa5dff0429d'
key = '431346910fd7435180c72f27b72c5f8d'
scene_descriptor.bootstrap_MSC(key)


try:
	# True for  getting button responses
	while True:
		print('Press a button')
		helper.output_audio('Press a button...')
		button_state1 = GPIO.input(pin1)
		button_state2 = GPIO.input(pin2)
		button_state3 = GPIO.input(pin3)

    	if button_state1 == False:
		print('Capture And Detect...')
		helper.output_audio('Capture And Detect...')
		# key = scene_descriptor.getKey()
        	try:
        		scene_descriptor.camera_PR(key, camera)
			scene_descriptor.camera_PR_DeepAI(_key_DeepAI, camera)
    		except:
        		print "Some Unknown Error"
        		helper.output_audio("Some Unknown Error")

		if button_state2 == False:
			print('OCR Activated...')
			helper.output_audio('OCR Activated...')
			# time.sleep(0.2)
			imageName = r'./abc.jpg'
			camera.capture(imageName)
			print OCR.get_string('./' + imageName)
			helper.output_audio('./' + imageName)

		if button_state3 == False:
			print('Sending Emergency Message...')
			helper.output_audio('Sending Emergency Message...')
			time.sleep(0.2)

except:
    GPIO.cleanup()
