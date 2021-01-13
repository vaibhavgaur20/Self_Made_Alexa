import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import sys
import webbrowser
import bs4

# from googlesearch.googlesearch import GoogleSearch

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'ai' in command:
            command = command.replace('ai', '')

        return command






def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        search = command.replace('what is', '')
        print('Searching ',search)
        # search = search + 'in advance database administrator'
        # info = wikipedia.summary(search, 1)
        res = requests.get('https://www.google.com/search?q=vigilante+mic'+''.join(search))
        print('res ', res)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,"html.parser")
        # print('soup ', soup)
        linkElements = soup.select('a')
        print('link ', linkElements)
        linkToOpen = min(1, len(linkElements))
        print('linktoOpen', linkToOpen)

        for i in range(linkToOpen):
            webbrowser.open('https://google.com'+linkElements[i].get('href'))
        # print(info)
        # talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()