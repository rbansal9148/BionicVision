import boot
import helper
from time import sleep

boot.internet_on() #If no connection to MCS is established than it will exit
print "Waiting 2 secs"
#sleep(2)
boot.isMCSWorking()

