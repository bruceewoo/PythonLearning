#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import webbrowser as wb
import os

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    sentence = r.recognize_google(audio)
    print("You said: " + sentence)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

words = sentence.split(" ")
for website in words:
    url = "www.{0}.com".format(website)
    os.system(r"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome {0}".format(url))
