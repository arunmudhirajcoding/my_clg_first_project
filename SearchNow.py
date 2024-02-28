# import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# it is to choice the voice (male[0] , female[1])

engine.setProperty('voice', voices[1].id)
# engine.setProperty('voice', voices[0].id)

# The function is used to exit from the code or to shutdown the program AI
def shutDown():
    sys.exit()

# it gives the audio to AI
def speak(audio):
    engine.say(audio)
    engine.runAndWait()