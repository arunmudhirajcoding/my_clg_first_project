import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyaudio
# import numpy as np
import noisereduce as nr
# import sounddevice as sd

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

# This cancels the noise around the system
def reduce_noise(audio_data, sample_rate):
    # Reduce noise
    return nr.reduce_noise(y=audio_data, sr=sample_rate)

# Modified audio will be delivered
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,
                        input=True, frames_per_buffer=1024)
    print("Recording...")
    frames = []
    for _ in range(0, int(44100 / 1024 * 5)):  # Adjust the duration as needed
        data = stream.read(1024)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    return b''.join(frames)

# this function helps to listens users voice and commands or query's
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    return recognizer, audio

# this function helps to understands users voice and commands or query's
def recognize_speech(recognizer, audio):
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower() # if the voice has upper case it convert into lower case
    
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return "None"
    except sr.RequestError:
        print("Sorry, I couldn't request results. Please check your internet connection.")
        return "None"


if __name__ == "__main__":

    from WishME import  wish_me
    wish_me()
    while True:
        query = recognize_speech(*listen())

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music = 'C:\\songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\durug\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "go to sleep" in query:
            speak("going to sleep, run again to wake me anytime u need")
            print("sleeping😴😴😴zzzzz.....")
            shutDown()
