

from Functions import *
from SIVRAJ import *
#Notations = music(200, "Yaman")

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("what do you want to search?")
            print("F.R.I.D.A.Y.:What do you want to search?")
            searchYoutube = takeCommand()
            webbrowser.open('https://www.youtube.com/results?search_query=' + searchYoutube)


        elif 'open google' in query:
            speak("what do you want to search?")
            print("F.R.I.D.A.Y.:What do you want to search?")
            searchGoogle = takeCommand()
            webbrowser.open('https://www.google.com/?#q=' + searchGoogle)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'play music'in query:
            speak("How many notes do you want to play?")
            notes = int(input("No. of notes :"))
            speak("Which raag do you want to play?")
            rg = input("Raag :")
            music(notes, rg)


        elif 'exit' in query:
            print("See you later!")
            speak("See you later!")
            break
