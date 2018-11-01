# The main script for the lighting system
# Author: Rihards Belinskis
# Project: Home Automation

import speech_recognition as sr
import subprocess

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    while True:
        try:
            text = r.recognize_google(audio)
            print("Command : {}".format(text))
        except:
            print("Unrecognized command.")

        if text == "lights on":
            print("Let there be light!")
            subprocess.call("lights.py")
        else:
            print('Unrecognized command. Try again!')
