import datetime
import os
import webbrowser
from random import random
from webbrowser import get

import pyttsx3
import speech_recognition
from pyjokes import pyjokes
from wikipedia import wikipedia

engine = pyttsx3.init("sapi5")
voices: object = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# rate = engine.setProperty("rate", 170)

# to voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# voice convert to text
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        speak("Say that again")
        return "None"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening")
        print("I am Jarvis sir How can i help you ?")
    speak("I am Jarvis sir How can i help you ?")


if __name__ == "__main__":
    wish()
    id = 50

    query = takeCommand().lower()

    #     logic building to task
    # Open Notepad
    if "open Notepad" in query:
        enpath = "C:\\Windows\\system32\\notepad.exe"
        os.system(enpath)
        speak("Opening Notepad")

        # Open Chrome
    elif "open Chrome" in query:
        apath = "C:\\Users\\Administrator\\Desktop\\Safiqul Islam - Chrome.lnk"
        os.system(apath)
        speak("Opening Chrome")

        # Open Code
    elif "open code" in query:
        bpath = "C:\\Users\\Administrator\\Desktop\\Visual Studio Code.lnk"
        os.system(bpath)
        speak("Opening Code Studio")
        # Open OBS

    elif "open OBS" in query:
        cpath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
        os.system(cpath)
        speak("Opening OBS Studio")
        # Open Pycharm
    elif "open code 2" in query:
        dpath = "C:\\Users\\Public\\Desktop\\PyCharm 2023.3.4.lnk"
        os.system(dpath)
        speak("Opening PyCharm")
        # Open Notion
    elif "open notion" in query:
        epath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Notion\\Notion.exe"
        os.system(epath)
        speak("Opening Notion")
        # Open CMD
    elif 'open CMD' in query:
        os.system("start cmd")
        speak("Opening CMD")
        # Play Music
    elif "open music play" in query:
        music_dir = "G:\\mu\\"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Opening Songs")
        # My IP Address
    elif 'my IP address' in query:
        ip = get("https://api.ipify.org").text
        speak(f"Your Ip Address is{ip}")
        # Searching Wikipedia
    elif 'Wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=4)
        speak(results)
        print(results)

    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
        speak("Opening Youtube ")
        # Web
    elif 'open facebook' in query:
        webbrowser.open("www.facebook.com")
        speak("Opening Facebook ")
        # Web
    elif 'open router' in query:
        webbrowser.open("192.168.0.1")
        speak("Opening Router Page ")
        # Web
    elif 'open chat gpt' in query:
        webbrowser.open("https://chat.openai.com/")
        speak("Opening Chat GPT ")
        # Web
    elif 'open chat gpt' in query:
        webbrowser.open("https://chat.openai.com/")
        speak("Opening chat GPT ")
        # Web
    elif 'open chat gvt' in query:
        webbrowser.open("https://chat.openai.com/")
        speak("Opening chat GPT ")
        # Web
    elif 'open Wi-Fi speed check' in query:
        webbrowser.open("www.fast.com")
        speak("Opening Fast Speed Check ")
        # Web
    elif 'open Faria web' in query:
        webbrowser.open("www.jannatulfaria.xyz")
        speak("Opening Your Faria Web Page ")
        # Web
    elif 'open Ustad' in query:
        webbrowser.open("https://ostad.app/dashboard/my-courses")
        speak("Opening Ostad Dashboard ")
        # Tell The Time
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")
        # Close Notepad
    elif "close Notepad" in query:
        speak("Ok Sir Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "set alarm " in query:
        nn = int(datetime.datetime().hour)
        if nn == 22:
            music_dir = "G:\\mu\\"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        # tell joke
    elif "tell me a Joke" in query:
        joke = pyjokes.get_jokes()
        speak(joke)

        # Shutdown The System
    elif "shutdown the system" in query:
        # os.system("shutdown /s /t 5")
        speak("Ok Sir Shutting Down")

        # Restarting The System
    elif "restart the system" in query:
        # os.system("shutdown /r /t 5")
        speak("Restarting the system")
        # Sleeping the system
    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendedState 0,1,0")
        speak("Ok Sir Sleeping the system")
        # Search Google
    elif 'search Google' in query:
        speak("Sir What Should i Search on google")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")
    # Exit
    # elif 'you can sleep' in query:
    #     speak("Thank you for using me sit, Have a nice day")
    #     sys.exit()
    # <Same>
    # elif 'no' in query:
    #     speak("Thank you for using me sit, Have a nice day")
    #     sys.exit()

    speak("Sir, do You have other Work ?")
query = takeCommand()
