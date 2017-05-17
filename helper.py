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
