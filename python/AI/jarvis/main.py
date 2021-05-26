# import libraries
import requests
import bs4
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis....")


MASTER = "Nibodh"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# This function makes the AI speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Initializing Jarvis...")
    if hour >= 0 and hour < 12:
        speak('Good Morning... ' + MASTER +' ...how may I help you?')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon...' + MASTER + '...how may I help you?')
    else:
        speak('Good Evening...' + MASTER + '...how may I help you?')
# This function will give commands to the AI

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please')
        query = None
    return query
def main():
    # main proggram starts here...
    
    wishMe()
    query = takeCommand()

    # logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open_new_tab("http://www.youtube.com")

    elif 'open google' in query.lower():
        webbrowser.open_new_tab("http://www.google.com")

    elif 'open google drive' in query.lower():
        webbrowser.open_new_tab("https://drive.google.com/drive/my-drive")

    elif 'play matrix' in query.lower():
        songs_dir = "F:\\media\\movies\\english\\action\\matrix\\The Matrix (1999)"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strtime}")

    # elif 'in google' in query.lower():
    #      query = query.replace('in google', "")
    #      res = requests.get('http://www.google.com/search?q=' + "".join(sys.argv[1:]))
    #      res.raise_for_status()
    #      soup = bs4.BeautifulSoup(res.text, "html.parser")
    #      linkElements = soup.select('.r a')
    #      linksToOpen = int(min(5, len(linkElements)))
    #      for i in range(linksToOpen):
    #          webbrowser.open_new_tab('http://www.google.com'+ linkElements[i].get('href'))
     
main()
