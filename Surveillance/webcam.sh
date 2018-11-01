# Shell script for the surveillance system
# Author: Rihards Belinskis
# Project: Home Automation
#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /your_URL/$DATE.jpg
mpack -s "ALERT! UNWANTED GUEST!" /your_URL/$DATE.jpg e-mail@domain.com
