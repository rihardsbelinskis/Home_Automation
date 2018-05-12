# Shell script for the 116 surveillance system
# Author: Rihards Belinskis
# Project: Home Automation
#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/Desktop/116Control/webcam/$DATE.jpg
mpack -s "ALERT! UNWANTED GUEST!" /home/pi/Desktop/116Control/webcam/$DATE.jpg e-mail@domain.com
