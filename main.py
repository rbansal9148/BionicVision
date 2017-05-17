import boot
import helper
from time import sleep

boot.internet_on() #If no connect to AWS is established than it will exit

helper.output_audio('Hello World')
