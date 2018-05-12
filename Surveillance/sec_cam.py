# The main script for the 116 surveillance system
# Author: Rihards Belinskis
# Project: Home Automation

import RPi.GPIO as GPIO
import time
import subprocess
from subprocess import call

GPIO.setmode(GPIO.BCM)
PIR_PIN = 10
GPIO.setup(PIR_PIN, GPIO.IN)

try:
        print "116 Surveillance System (CTRL+C to exit)"
        time.sleep(2)
        print "I can see you now!"
        while True:
                if GPIO.input(PIR_PIN):
                        print "Motion Detected!"
                        subprocess.call("./webcam.sh", shell = True)
                time.sleep(1)
except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
