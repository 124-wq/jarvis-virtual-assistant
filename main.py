#as keyword: helps us in substituting the whole word speech recognition to sr we can use this short keyword in our code to access speech recognition functions
#web browser module: helps us to open a web browser to a specific url  its a built in module
#we have to make a recognizer object to recognize the speech it will recognize the speech and convert it into text
#sr.Recognizer() this is a class that gives speech recognition functionality
#we need to also give command pip install pocketsphinx to install the pocketsphinx module which is used for offline speech recognition
# import client
import client
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine=pyttsx3.init() #initializes pyttsx
newsapi="21c3b2ba210540d3975f833ad2083226"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if c.lower()=="open google":
        speak("opening google")
        webbrowser.open("http://www.google.com")
    elif c.lower()=="open youtube":
        speak("opening youtube")
        webbrowser.open("http://www.youtube.com")
    elif c.lower()=="open microsoft edge":
        speak("opening microsoft edge")
        webbrowser.open("http://www.microsoft.com/edge")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        speak("opening news")
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get("articles",[])
            for ar in articles:
                speak(ar['title'])

    else:
        speak("processing your command")
        response=client.processcommand(c)
        speak(response)
        print(response)


if __name__ == "__main__":
    speak("initializing jarvis.....")
    while True:

        #listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
          

            

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source,timeout=5,phrase_time_limit=5)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("hey")
                #listen for commands
                with sr.Microphone() as source:
                  print("jarvis active...")
                  audio = r.listen(source)
                  command=r.recognize_google(audio)

                  processcommand(command)

            
        except sr.RequestError as e:
            print("google error; {0}".format(e))