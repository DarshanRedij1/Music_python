#!/usr/bin/env python
# coding: utf-8


# pip install pyttsx3
# pip install SpeechRecognition
# pip install wikipedia
# pip install pipwin
# pipwin install PyAudio



import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir. Please tell me how may I help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thershold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query







