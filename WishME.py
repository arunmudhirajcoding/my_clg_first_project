import datetime
import pyttsx3

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
    
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!, sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon!, sir")
    else:
        speak("Good Evening!, sir")
    speak("I am chitttti 3 point o. Please tell me how may I help you")
