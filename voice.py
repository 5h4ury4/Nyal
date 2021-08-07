#Importing module for speech.
import pyttsx3
#using sapi5 as a voice engine.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Making a audio function.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()