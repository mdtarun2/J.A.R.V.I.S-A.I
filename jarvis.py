# import os
# import sys
# import webbrowser
# from datetime import datetime
# import smtplib
# import kit
# from requests import get
# import pyttsx3
# import speech_recognition as sr
# import random
#
# from wikipedia import wikipedia
#
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voices", voices[0].id)
#
#
# # text To speech
# def speak(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()
#
#
# # to convert voice into text
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source, timeout=1, phrase_time_limit=5)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="en-in")
#         print(f"User said: {query}")
#
#     except Exception as e:
#         print("Say that again Please...")
#
#
# # to wish
# def wish():
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour <= 12:
#         speak("Good Morning")
#     elif 12 <= hour <= 18:
#         speak("Good Afternoon")
#
#     else:
#         speak("Good Evening")
#     speak("I am Jarvis . How can I help you?")
#
#
# # to send email
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login = ("Enter your Gmail", "Enter Your Password")
#     server.sendmail()
#     server.close()
#
#
# if __name__ == "__main__":
#     while True:
#         # if 1:
#
#         query = takeCommand()
#

#         speak("Sir, do You have other Work ?")
#

#
#


import os
import sys
import webbrowser
from datetime import datetime
import smtplib
from requests import get
import pyttsx3
import speech_recognition as sr
import random
from wikipedia import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


# text To speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 <= hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. How can I help you?")


# to convert voice into text
def takeCommand() -> object:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return ""  # Return empty string if timeout occurs


# to wish

if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand()

        if "open Notepad" in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.system(path)
            speak("Opening Notepad")

        elif "open Chrome" in query:
            path = "C:\\Users\\Administrator\\Desktop\\Safiqul Islam - Chrome.lnk"
            os.system(path)
            speak("Opening Chrome")

        elif "open code" in query:
            path = "C:\\Users\\Administrator\\Desktop\\Visual Studio Code.lnk"
            os.system(path)
            speak("Opening Code Studio")

        elif "open OBS" in query:
            path = "C:\\Users\\Public\\Desktop\\OBSStudio.lnk"
            os.system(path)
            speak("Opening OBS Studio")

        elif "open code 2" in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm 2023.3.4\\bin\\pycharm64.exe"
            os.system(path)
            speak("Opening PyCharm")

        elif "open notion" in query:
            path = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Notion\\Notion.exe"
            os.system(path)
            speak("Opening Notion")

        elif 'open CMD' in query:
            os.system("start cmd")
            speak("Opening CMD")

        elif "open music play" in query:
            music_dir = "G:\\mu\\"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Opening Songs")

        elif 'my IP address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your Ip Address is{ip}")

        elif 'Wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube ")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
            speak("Opening Facebook ")
        elif 'open router' in query:
            webbrowser.open("192.168.0.1")
            speak("Opening Router Page ")
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")
            speak("Opening Chat GPT ")
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")
            speak("Opening chat GPT ")
        elif 'open chat gvt' in query:
            webbrowser.open("https://chat.openai.com/")
            speak("Opening chat GPT ")
        elif 'open Wi-Fi speed check' in query:
            webbrowser.open("www.fast.com")
            speak("Opening Fast Speed Check ")
        elif 'open Faria web' in query:
            webbrowser.open("www.jannatulfaria.xyz")
            speak("Opening Your Faria Web Page ")
        elif 'open Ustad' in query:
            webbrowser.open("https://ostad.app/dashboard/my-courses")
            speak("Opening Ostad Dashboard ")
        elif 'search Google' in query:
            speak("Sir What Should i Search on google")
            cm = takeCommand().lower()
            webbrowser.open("https://www.google.com/search?q=")

        elif 'no thank you' in query:
            speak("Thank you for using me sit, Have a nice day")
            sys.exit()
        elif 'no thank u' in query:
            speak("Thank you for using me sit, Have a nice day")
            sys.exit()
        elif 'no thanks' in query:
            speak("Thank you for using me sit, Have a nice day")
            sys.exit()
        elif 'no thanks' in query:
            speak("Thank you for using me sit, Have a nice day")
            sys.exit()
        elif 'no' in query:
            speak("Thank you for using me sit, Have a nice day")
            sys.exit()

        speak("Sir, do You have other Work ?")
query = takeCommand()
