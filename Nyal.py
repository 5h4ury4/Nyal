#Importing modules
from tkinter import *
import voice
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import ctypes
import os

#Adding the canvas
nyal = Tk()
canvas = Canvas(nyal, width = 1920, height = 1080)
nyal.state("zoomed")
#Adding the Nyal image to the program.
photo = PhotoImage(file='nyalimg.png')
shot = Label(nyal, image=photo)
shot.pack()
#Adding the logo.
logo = PhotoImage(file="nyal.png")
nyal.iconphoto(False, logo)
#Adding a title.
nyal.title("Nyal")
#For debugging.
#voice.speak("HEllo World")

def version():
    voice.speak("This is the first build of this program this will be updated.")

#Fuction to wish the user.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        voice.speak("Good Morning!")
    elif hour>=12 and hour<18:
        voice.speak("Good Afternoon!")   
    else:
        voice.speak("Good Evening!")  
        voice.speak("I am Nyal. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        #print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        #print(f"User said: {query}\n")

    except Exception as e:    
        #print("Say that again please...")  
        voice.speak("Say that again please...")
        return "None"
    return query
#Adding a variable to run AI engine.
shaurya = True
#Adding the to-do list.
text = Text()
#text.configure()
text.pack()
version()
canvas.pack()
#Starting the AI engine with an if and elif statement.
if shaurya == True:
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            voice.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            voice.speak("According to Wikipedia")
            #print(results)#Enable for debugging
            voice.speak(results)
            text.delete("1.0","end")
            text.insert(INSERT, results)
            #Opening Youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            text.delete("1.0","end")
            voice.speak("Opened YouTube.")
            text.insert(INSERT, "Opened YouTube.")
            #Opening google
        elif 'open google' in query:
            webbrowser.open("google.com")
            #Opening Stackoverflow
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   
            #Command to tell the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            voice.speak(f"Sir, the time is {strTime}")
            #Command for opening visual studio code
        elif 'open code' in query:
            codePath = "C:\\Users\\shotb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            #Command to lock the PC
        elif 'lock' in query:
            ctypes.windll.user32.LockWorkStation()
            #Command to exit the program
        elif 'quit' in query:
            voice.speak("It's been a pleasure to help you....")
            exit()

nyal.mainloop()