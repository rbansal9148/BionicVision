import boot
import helper
from time import sleep

boot.internet_on() #If no connection to AWS is established than it will exit
print "Waiting 2 secs"
sleep(2)
boot.isAWSWorking()

