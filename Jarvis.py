import pyttsx3 #pip install pyttsx3
import speech_recognition as sr#pip install speechRecognition
import wikipedia
import datetime
import pyaudio
import webbrowser
import os


engine = pyttsx3.init("sapi5") #sapi 5 is microsoft speech api
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

  

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning, how are you doing")
    else:
        speak("welcome back sir")
    speak("how may i help ,sir")



def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print("Recoginzing ")
        query=r.recognize_google(audio,language="en-US")
        print(f"you:{query}\n")
    except Exception as e:
        print(e)
        speak("sorry for inconvenience , please say that again")
        return "None"
    return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("http://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("http://www.google.com")
        elif 'play music'  in query:
            musicdir = 'F:\\MOVIES & music\\Songs' 
            songs= os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[3]))